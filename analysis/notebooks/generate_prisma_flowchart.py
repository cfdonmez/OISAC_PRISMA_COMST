"""
PRISMA 2020 Flow Diagram Generator
==================================
This script generates a standard PRISMA 2020 flow diagram using the Graphviz library.
It visualizes the flow of information through the different phases of a systematic review.

Usage:
    python generate_prisma_flowchart.py

Requirements:
    - python-graphviz (pip install graphviz)
    - Graphviz system binary (https://graphviz.org/download/)

Author: Antigravity
Date: 2025-12-09
"""

import os
import sys

def check_graphviz():
    """Checks if graphviz is importable."""
    try:
        import graphviz
        return graphviz
    except ImportError:
        print("Error: The 'graphviz' python library is not installed.")
        print("Please run: pip install graphviz")
        sys.exit(1)

def generate_prisma_dot(data):
    """
    Defines the Graphviz Digraph structure for PRISMA 2020.
    """
    graphviz = check_graphviz()
    
    dot = graphviz.Digraph('PRISMA_2020', comment='PRISMA 2020 Flow Diagram')
    dot.attr(rankdir='TB', splines='ortho', nodesep='0.8', ranksep='0.6', compound='true')
    
    # Global Node Styles
    dot.attr('node', shape='box', style='filled', fillcolor='#f9f9f9', 
             fontsize='11', fontname='Arial', penwidth='1.5', margin='0.2')
    dot.attr('edge', arrowhead='vee', arrowsize='0.8', color='#333333')

    # ------------------------------------------------------------------
    # PHASE 1: IDENTIFICATION
    # ------------------------------------------------------------------
    with dot.subgraph(name='cluster_identification') as c:
        c.attr(label='Identification', style='dashed', color='#aaaaaa', fontcolor='#aaaaaa', labeljust='l')
        
        # Nodes
        records_db_label = f"Records identified from:\\nDatabases (n = {data['identified_databases']})\\nRegisters (n = {data['identified_registers']})"
        c.node('id_databases', label=records_db_label, width='3.5', fillcolor='#e1f5fe')
        
        duplicates_label = f"Records removed before screening:\\nDuplicate records removed (n = {data['duplicates_removed']})"
        c.node('calc_duplicates', label=duplicates_label, width='3.5')
        
        c.edge('id_databases', 'calc_duplicates')

    # ------------------------------------------------------------------
    # PHASE 2: SCREENING
    # ------------------------------------------------------------------
    with dot.subgraph(name='cluster_screening') as c:
        c.attr(label='Screening', style='dashed', color='#aaaaaa', fontcolor='#aaaaaa', labeljust='l')
        
        screened_label = f"Records screened\\n(n = {data['records_screened']})"
        c.node('screened', label=screened_label, width='3.5', fillcolor='#fff3e0')
        
        excluded_label = f"Records excluded\\n(n = {data['excluded_title_abstract']})"
        c.node('excluded_screening', label=excluded_label, width='3.5')
        
        retrieved_label = f"Reports sought for retrieval\\n(n = {data['retrieved_full_text']})"
        c.node('retrieved', label=retrieved_label, width='3.5', fillcolor='#fff3e0')
        
        not_retrieved_label = f"Reports not retrieved\\n(n = {data['not_retrieved']})"
        c.node('not_retrieved', label=not_retrieved_label, width='3.5')
        
        assessed_label = f"Reports assessed for eligibility\\n(n = {data['assessed_full_text']})"
        c.node('assessed', label=assessed_label, width='3.5', fillcolor='#fff3e0')
        
        # Excluded with reasons
        reasons_text = "\\n".join([f"{k} (n = {v})" for k, v in data['reasons_excluded'].items()])
        excluded_full_label = f"Reports excluded:\\n{reasons_text}"
        c.node('excluded_full', label=excluded_full_label, width='3.5', justify='l')
        
        # Edges
        c.edge('screened', 'excluded_screening', constraint='false') # Side arrow
        c.edge('retrieved', 'not_retrieved', constraint='false')     # Side arrow
        c.edge('assessed', 'excluded_full', constraint='false')      # Side arrow

    # ------------------------------------------------------------------
    # PHASE 3: INCLUDED
    # ------------------------------------------------------------------
    with dot.subgraph(name='cluster_included') as c:
        c.attr(label='Included', style='dashed', color='#aaaaaa', fontcolor='#aaaaaa', labeljust='l')
        
        included_label = f"Studies included in review\\n(n = {data['included_studies']})"
        c.node('included', label=included_label, width='3.5', fillcolor='#e8f5e9')

    # Main Flow Edges
    dot.edge('calc_duplicates', 'screened')
    dot.edge('screened', 'retrieved')
    dot.edge('retrieved', 'assessed')
    dot.edge('assessed', 'included')
    
    # Invisible constraints for side-by-side layout alignment (optional tuning)
    with dot.subgraph() as s:
        s.attr(rank='same')
        s.node('screened')
        s.node('excluded_screening')
        s.edge('screened', 'excluded_screening', style='invis')
        
    with dot.subgraph() as s:
        s.attr(rank='same')
        s.node('retrieved')
        s.node('not_retrieved')
        s.edge('retrieved', 'not_retrieved', style='invis')
        
    with dot.subgraph() as s:
        s.attr(rank='same')
        s.node('assessed')
        s.node('excluded_full')
        s.edge('assessed', 'excluded_full', style='invis')

    return dot

def main():
    # Define paths
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(base_dir, '../../data/figures')
    os.makedirs(output_dir, exist_ok=True)
    
    # ------------------------------------------------------------------
    # TODO: Connect this to actual CSV logs in future steps
    # For now, using Placeholder Data consistent with user's project findings
    # ------------------------------------------------------------------
    mock_data = {
        "identified_databases": 1200,   # Example
        "identified_registers": 0,
        "duplicates_removed": 400,
        "records_screened": 800,
        "excluded_title_abstract": 642,
        "retrieved_full_text": 158,     # The number of included studies implies these were retrieved
        "not_retrieved": 0,
        "assessed_full_text": 158,      # Assuming all retrieved were assessed
        "excluded_full_text": 0,        # Update when full-text screening is logged
        "reasons_excluded": {           # Example reasons
            "Wrong Domain": 0,
            "No Full Text": 0
        },
        "included_studies": 158         # Matches the user's "158 included studies" count
    }
    
    print("Generating PRISMA Flow Diagram with current project stats...")
    
    try:
        dot = generate_prisma_dot(mock_data)
        output_path = os.path.join(output_dir, 'PRISMA_2020_flow_diagram')
        
        # Render PDF and PNG
        dot.render(output_path, format='png', cleanup=True)
        dot.render(output_path, format='pdf', cleanup=True)
        
        print(f"Success! Diagram saved to:\n  - {output_path}.png\n  - {output_path}.pdf")
        
    except Exception as e:
        print(f"\n[ERROR] Failed to render graph. Ensure Graphviz is installed on your system.")
        print(f"Details: {e}")
        print("\nFix: Install Graphviz from https://graphviz.org/download/ and add to PATH.")

if __name__ == "__main__":
    main()
