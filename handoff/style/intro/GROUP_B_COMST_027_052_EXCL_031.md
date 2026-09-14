# Full Introduction Audit — Group B (COMST_027–COMST_052, excluding COMST_031)

## Scope and method

This audit covers every true IEEE *Communications Surveys & Tutorials* article in the local corpus from `COMST_027` through `COMST_052`, with `COMST_031` excluded because it is an IEEE *Wireless Communications* article rather than a COMST article. The resulting coverage is **25/25 eligible introductions**:

`COMST_027`, `COMST_028`, `COMST_029`, `COMST_030`, `COMST_032`, `COMST_033`, `COMST_034`, `COMST_035`, `COMST_036`, `COMST_037`, `COMST_038`, `COMST_039`, `COMST_040`, `COMST_041`, `COMST_042`, `COMST_043`, `COMST_044`, `COMST_045`, `COMST_046`, `COMST_047`, `COMST_048`, `COMST_049`, `COMST_050`, `COMST_051`, and `COMST_052`.

For each article, the complete Introduction was read from its Introduction heading through the heading of the next numbered main section. Embedded tables, figures, author metadata, page-break fragments, and footnotes were inspected as part of the local extraction but were not treated as prose paragraphs. The notes below paraphrase narrative functions; no source sentence is reproduced as a reusable template.

### Extraction qualifications

- The Markdown conversion often drops the decorated initial letter of the first word (for example, an opening word may appear without its first character). This is an extraction artifact, not an author-style feature.
- Page furniture and author metadata interrupt some paragraphs, particularly near the first page break. Paragraph meaning was reconstructed across those interruptions.
- Mojibake, line-end hyphenation, malformed table symbols, and duplicated tokens occur in several files. These were ignored when judging the underlying rhetorical design.
- `COMST_040` and `COMST_050` have unusually long Introductions; their Introduction subsections were read in separate contiguous chunks to avoid output truncation.
- `COMST_034` moves its extended survey comparison into Section II. Only the compact comparison and gap statement that remain in Section I are classified below as Introduction prose.

## Article-by-article narrative maps

### COMST_027 — Beyond-diagonal reconfigurable intelligent surfaces

- **Paragraph-function sequence:** broad 6G requirements → RIS as one candidate technology → conventional RIS definition and practical appeal → academic, industrial, and standardization maturity → the diagonal scattering-matrix limitation → a concrete mathematical question → BD-RIS as the answer → circuit and element-arrangement degrees of freedom → application vision → limited prior overviews → tutorial gap → six contributions → organization and notation.
- **Transition mechanisms:** scale narrows through “among the candidate solutions”; the pivotal turn is contrastive (“despite” the progress, a structural limitation remains); a displayed matrix and a direct engineering question create the hinge from D-RIS to BD-RIS; “the answer” introduces the new paradigm; prior-work coverage then moves to a tutorial gap.
- **Tone and rhythm:** technically authoritative and pedagogical, with long explanatory paragraphs followed by short emphatic turns. The mathematical hinge gives the Introduction momentum despite its length.
- **Related work, gap, contribution, organization:** related overview papers are summarized late and compactly in a table; the gap is not merely “few papers” but the absence of a rigorous tutorial linking microwave foundations, signal processing, impairments, benefits, and applications. Contributions are extensive and numbered rhetorically; the roadmap is conventional and detailed.
- **Strong pattern:** make the novelty intelligible through a concrete object and limitation before claiming a literature gap.
- **Pattern not to imitate:** the contribution list is longer than needed, and the roadmap contains a section-order inconsistency in the extracted text. The repeated “first/second/third” pattern becomes mechanical.

### COMST_028 — Active reconfigurable intelligent surfaces

- **Paragraph-function sequence:** broad wireless/6G progress → passive RIS benefits → multiplicative-fading mechanism and inadequate remedies → ARIS mechanism → prototype and numerical evidence → analog implementation and practical constraints → additional benefits → long survey catalogue and comparison table → ARIS-specific gap → motivation → four contributions → organization.
- **Transition mechanisms:** “yet” turns general enthusiasm into a physical limitation; “in this context” introduces ARIS; comparison with passive RIS sustains the explanation; “however” marks the literature gap; the text then shifts explicitly to motivation and contributions.
- **Tone and rhythm:** promotional and expansive. Many sentences reiterate transformation, benefits, and comprehensiveness. Quantitative prototype examples briefly restore specificity.
- **Related work, gap, contribution, organization:** prior surveys are handled largely paper by paper and repeated after an already dense table. The gap is an ARIS-focused survey. Contributions cover fundamentals, applications, comparisons, and open problems; the roadmap is short.
- **Strong pattern:** the passive-versus-active physical mechanism supplies a real reason for the topic.
- **Pattern not to imitate:** catalogue-style related work, repeated novelty language, and claims of uniqueness without a sharply bounded comparison axis. Publication in COMST does not make these habits a house-style requirement.

### COMST_029 — Machine-learning-driven cognitive radio

- **Paragraph-function sequence:** historical communication progress → growing spectrum pressure → CR as an access solution → why awareness alone is not cognition → ML as learning/adaptation → use across several spectrum-hungry network families → long related-work review by domain → domain-by-domain omissions → consolidated cross-domain gap → contributions → organization.
- **Transition mechanisms:** the narrative repeatedly moves problem → candidate solution → residual limitation. “Nevertheless” distinguishes awareness from learning; application paragraphs use the common spectrum problem to connect otherwise different domains; the gap is built by progressively eliminating what adjacent surveys cover.
- **Tone and rhythm:** explanatory and accessible in the opening, then bibliographic and heavy in the related-work block. The prose regains direction in the Motivation subsection.
- **Related work, gap, contribution, organization:** related surveys are grouped first by CR/ML focus and then by application domain, but many individual summaries slow the argument. The eventual gap is clear: no single review connects ML-driven CR across IoT, mobile, vehicular, railway, and UAV systems. Contributions and roadmap mirror that taxonomy.
- **Strong pattern:** use a shared engineering constraint to justify bringing multiple application families into one survey.
- **Pattern not to imitate:** exhaustive one-paper-per-sentence review in the Introduction and broad audience-value assertions such as calling the survey indispensable or invaluable.

### COMST_030 — Aerospace integrated networks for 6G

- **Paragraph-function sequence:** device growth and coverage inequality → space access and AIN definition → constellation deployment evidence → single-tier to heterogeneous multi-tier motivation → heterogeneity and resource-management problems → standards, industrial, and research activity → prior surveys by individual and integrated tiers → fragmentation gap → intended integrative reference model → five content axes and organization → explanation of how the axes form one framework.
- **Transition mechanisms:** quantitative scale establishes urgency; “although” turns deployment growth into unresolved architecture questions; standards and industrial programs demonstrate maturity; “however” converts the survey catalogue into a multi-tier gap; the final passage explains dependencies among architecture, modeling, optimization, and future directions.
- **Tone and rhythm:** ambitious, encyclopedic, and highly list-driven. Tables carry substantial context, but prose often repeats their content.
- **Related work, gap, contribution, organization:** the comparison distinguishes single-tier surveys from integrated-network surveys. The gap is broad but intelligible: partial or disconnected coverage of heterogeneous AIN layers. Contributions are embedded in an unusually detailed organization section.
- **Strong pattern:** the survey architecture is explained as a dependency chain rather than only a list of section titles.
- **Pattern not to imitate:** very long inventories of constellations, organizations, and adjacent surveys before the main gap; grammatical density and repeated “systematic/comprehensive” wording weaken the voice.

### COMST_032 — IEEE 802.11bf WLAN sensing

- **Paragraph-function sequence:** Wi-Fi maturity and economic reach → physical mechanism by which Wi-Fi signals reveal the environment → RSSI and CSI sensing history → comparison with other sensing technologies → infrastructure-reuse advantages → concrete deficiencies in commercial Wi-Fi sensing → need for standard support → role of IEEE 802.11bf → distinction from device-assisted ranging in 802.11az → limitations of earlier 802.11bf overviews → present scope → detailed organization.
- **Transition mechanisms:** physical explanation turns familiarity with Wi-Fi into sensing plausibility; repeated comparisons distinguish measurement bases; “despite the benefits” introduces implementation barriers; “to solve” those barriers motivates standardization; “in contrast” separates sensing from ranging; prior papers are assessed against named missing technical components.
- **Tone and rhythm:** tutorial and standards-oriented, precise rather than promotional. It is long because it supplies both the physical motivation and amendment-specific context.
- **Related work, gap, contribution, organization:** related works are evaluated against sub-7-GHz/60-GHz procedures, technical features, models, and future directions. The gap is feature-specific. Contributions are expressed as the paper’s promised coverage rather than a conspicuous bullet list; the roadmap is very detailed.
- **Strong pattern:** motivate a survey with operational obstacles and standard-design consequences, not with popularity alone.
- **Pattern not to imitate:** extensive modality-by-modality background and section-by-section roadmap may be excessive when the audience does not need a standards tutorial.

### COMST_033 — Beam alignment in mmWave V2X

- **Paragraph-function sequence:** autonomous-vehicle relevance → data-sharing demands beyond sub-6-GHz capability → mmWave benefits → directional beams as the response to path loss → mobility/blockage/training make beam alignment unusually hard in V2X → related surveys across mmWave and vehicular communication → missing beam-alignment, metric, and future-direction coverage → focused contributions → organization.
- **Transition mechanisms:** “nevertheless” and “unfortunately” expose insufficiency; “here” introduces mmWave; a second “nevertheless” converts mmWave’s benefit into its beam-alignment cost; comparison with generic mobility isolates what is V2X-specific; “distinguished from” introduces scope.
- **Tone and rhythm:** problem-led and generally readable, with a strong benefits-versus-cost structure. The extracted prose contains a duplicated phrase and occasional inflated adjectives.
- **Related work, gap, contribution, organization:** adjacent surveys are clustered by topic and summarized with a matrix. The gap is a narrow intersection—beam alignment specifically in mmWave V2X—with explicit metric coverage. Contributions follow that same intersection.
- **Strong pattern:** every scope decision grows out of a physical or operational constraint.
- **Pattern not to imitate:** “first paper” assertions and adjective-heavy claims should be used only when reproducibly verified.

### COMST_034 — Computational intelligence for UAV swarm networking and collaboration

- **Paragraph-function sequence:** growth and advantages of UAV swarms → networking as one requirement → collaboration as a second requirement → dynamic missions defeat conventional methods → computational intelligence as an adaptive tool → prior surveys split between networking and collaboration → static versus dynamic problem-solving distinction → dual-gap statement → survey scope and three contributions → organization.
- **Transition mechanisms:** paired “on the one hand/on the other hand” paragraphs establish two coequal axes; “however” introduces dynamic complexity; “fortunately” introduces CI; the prior-survey split mirrors the two axes; “in fact” deepens the gap from subject coverage to problem-solving logic.
- **Tone and rhythm:** direct, moderately technical, and more compact than many corpus papers. The main literature details are wisely deferred to Section II.
- **Related work, gap, contribution, organization:** the Introduction names two survey classes and states what each omits; the full comparison follows outside the Introduction. The contribution is simultaneous treatment plus a four-way algorithm taxonomy; the roadmap is standard.
- **Strong pattern:** a two-axis opening can justify a genuinely integrative survey when both axes later organize the synthesis.
- **Pattern not to imitate:** novelty claims based on “to the best of our knowledge” still need a transparent comparison table and date boundary.

### COMST_035 — Backdoor attacks and defenses in wireless federated learning

- **Paragraph-function sequence:** wireless AI and privacy problem → federated learning mechanism and benefits → non-IID data and robustness weakness → attack taxonomy → reason to focus on backdoors → real-world analogies and emerging WFL attacks → wireless-medium-specific exposure → partial defenses and remaining problem → motivation → existing-survey gap → scope and contributions → organization.
- **Transition mechanisms:** “despite its merits” is the main reversal; progressively narrower paragraphs move from adversarial attacks to backdoors to WFL-specific backdoors; examples make stealth tangible; “however” marks limited defenses; the Motivation subsection restates why the threat deserves a survey.
- **Tone and rhythm:** sober in its technical passages but occasionally sensational in external examples. Long enough to establish a threat model before related work.
- **Related work, gap, contribution, organization:** a comparison matrix distinguishes attack/defense depth, mathematical mechanisms, applicability, limitations, and wireless-channel treatment. The gap is explicitly WFL- and wireless-network-aware. Contributions align with attack taxonomy, defense taxonomy, comparisons, and open issues.
- **Strong pattern:** narrow the threat surface step by step and make the survey boundary explicit.
- **Pattern not to imitate:** loosely analogous incidents and rapidly changing examples can age badly or imply evidence stronger than the cited source provides.

### COMST_036 — Trust management for underwater wireless sensor networks

- **Paragraph-function sequence:** marine-resource importance → UWSNs and their applications → why underwater communication differs from terrestrial WSNs → hostile deployment and limits of conventional security → promise of trust mechanisms → environmental and organizational complexity of trust management → contributions → organization.
- **Transition mechanisms:** “however” introduces the acoustic-medium difference; a second contrast shows why encryption/authentication alone is insufficient; enumerated physical, operational, and multi-organization factors justify a dedicated trust framework.
- **Tone and rhythm:** steady, formal, and tutorial-like. The prose remains domain-specific and avoids a long survey catalogue in Section I.
- **Related work, gap, contribution, organization:** prior dedicated surveys are described only as limited in the Introduction; fuller related work is deferred to Section II. Contributions cover threats, trust concepts, evidence types, applications, model classes, and challenges; organization is conventional.
- **Strong pattern:** let environmental physics and deployment conditions explain why a generic framework cannot simply be transferred.
- **Pattern not to imitate:** a long six-item contribution list repeats several scope statements already made in prose.

### COMST_037 — Secure ISAC in 6G networks

- **Paragraph-function sequence:** 6G applications need physical-world perception → ISAC definition and technology drivers → IoT, sensor, and AI benefits → AI and network-integration security risks → prior ISAC reviews → missing algorithm/system/application/AI/framework integration → proposed unified architecture → five contributions → organization table.
- **Transition mechanisms:** opportunity and risk are interleaved rather than separated; each enabling technology is followed by a security or coordination cost; “however” turns related-work coverage into missing perspectives; the paper then pivots from survey to its own architecture proposal.
- **Tone and rhythm:** visionary and highly promotional, with coined layers and superlative descriptors. Technical topics are broad, but the thesis is diluted by simultaneous review and architecture invention.
- **Related work, gap, contribution, organization:** a feature matrix compares physical design, models, algorithms, architecture, systems, applications, and security. The gap is wide. Contributions mix evidence synthesis with original design claims; the roadmap is a large table.
- **Strong pattern:** pair every claimed integration benefit with a concrete security implication.
- **Pattern not to imitate:** “groundbreaking,” “unparalleled,” and similarly unbounded novelty language; also avoid allowing an original architecture proposal to obscure what the survey evidence itself supports.

### COMST_038 — Evasion attacks and defenses in cyber-physical systems

- **Paragraph-function sequence:** CPS roles and layers → IoT/IIoT data growth and ML adoption → adversarial-attack taxonomy → concrete evasion example → why the CPS attack surface is unusually broad → physical/network entry-point model → shortage of integrated CPS evasion research → contributions and societal relevance → detailed related-survey critique → synthesized gaps → methodology → scope exclusions → terminology clarification → organization.
- **Transition mechanisms:** “as a result” connects connected devices to ML demand; “evidence indicates” introduces vulnerability; “moreover” broadens the attack surface; “while” and “yet” isolate the literature gap; later sections use explicit scope and terminology transitions rather than leaving boundaries implicit.
- **Tone and rhythm:** analytical, security-conscious, and mostly restrained. It becomes lengthy because the Introduction contains related work, PRISMA-style selection, scope, and definitions.
- **Related work, gap, contribution, organization:** prior surveys are compared by knowledge setting, layer, taxonomy, balance, and feasibility. The gap is joint physical-plus-network treatment. Contributions precede the full related-work subsection, and the argument is partly repeated afterward. The roadmap is concise.
- **Strong pattern:** articulate the scope not only by inclusions but also by realistic exclusions and terminology rules.
- **Pattern not to imitate:** repeating the same gap before and after a long related-work block; detailed review methodology can pull the Introduction away from the survey’s technical story.

### COMST_039 — Evolution of non-terrestrial networks from 5G to 6G

- **Paragraph-function sequence:** traditional NTN uses → new aerospace economics and integration → terrestrial coverage limits → NTN augmentation → 3GPP/5G integration → 6G global-connectivity role → need for an integrated account → related surveys → multi-segment gap → four contribution axes → organization.
- **Transition mechanisms:** “however” marks the shift from traditional to integrated roles; economic and geographic limits motivate NTN complementarity; standardization then establishes timeliness; the related-work section uses “unlike” to differentiate the paper’s satellite/UAV/multi-segment breadth.
- **Tone and rhythm:** formal, comparatively compact, and framework-oriented. Its best passages use plain claims rather than slogans.
- **Related work, gap, contribution, organization:** a matrix precedes a concise account of the closest surveys. The contribution is organized along time evolution, protocol layers, evidence approach, and segment combinations—four genuine comparison dimensions. Organization follows those dimensions.
- **Strong pattern:** contributions are more persuasive when framed as independent analytical axes rather than synonyms for breadth.
- **Pattern not to imitate:** a long citation bundle of “less relevant” surveys adds little to the gap argument.

### COMST_040 — Holographic MIMO communications

- **Paragraph-function sequence:** 5G pillars and quantified 6G demands → mMIMO/mmWave/ultra-dense-network enablers → their physical and implementation limits → metamaterials, metasurfaces, and holography as the new route → definition of HMIMO → hardware and near-field qualitative changes → historical evolution → application vision → literature overview → exact limitations of existing reviews → six major contributions → organization.
- **Transition mechanisms:** “despite” turns successful 5G technologies into 6G limitations; “to fulfill” introduces the alternative; multiple conventional-versus-HMIMO contrasts explain qualitative change; history and vision widen context before the literature gap; the final “motivated by this status” links the comparison to the survey.
- **Tone and rhythm:** deep tutorial prose with high technical authority, but encyclopedic in scale. It alternates very long technical paragraphs with clear subsection headings.
- **Related work, gap, contribution, organization:** the literature overview distinguishes passive RIS, active HMIMO, near-field, hardware, and information-theory treatments. The gap is a panoramic account connecting physical implementation, theory, signal processing, and applications. Contributions are correspondingly broad and detailed.
- **Strong pattern:** explain a paradigm shift through changed assumptions—aperture continuity, mutual coupling, EM-domain processing, and near-field propagation—rather than by labels alone.
- **Pattern not to imitate:** a full historical tutorial and exhaustive source catalogue before the gap is unsuitable for a tighter survey Introduction.

### COMST_041 — Optical communications for deep space

- **Paragraph-function sequence:** human motive for space exploration → missions depend on communication → deep-space link constraints and observed rate limitations → FSO advantages and demonstrations → remaining technology dependencies → survey purpose → related-survey limitations → precise coverage gap → six contributions → organization.
- **Transition mechanisms:** a short bridge from exploration to communication establishes relevance; “unlike” differentiates deep space from terrestrial and near-Earth links; “compared to RF” introduces optical opportunity; “however” prevents the FSO argument from becoming promotional; “despite their valuable contributions” gives a fair gap transition.
- **Tone and rhythm:** natural, measured, and evidence-first. Paragraphs are neither uniformly short nor overloaded, and each advances the argument.
- **Related work, gap, contribution, organization:** related surveys are discussed by missing technical dimension and currency, not merely by title. The gap is holistic but itemized through an explicit comparison table. Contributions are concrete; organization is compact.
- **Strong pattern:** one of the strongest group exemplars—physical constraints, measured opportunity, fair literature positioning, and an unforced survey purpose form a coherent funnel.
- **Pattern not to imitate:** the “first discussion” claim on one topic still requires time-bounded verification.

### COMST_042 — In-network machine learning using programmable devices

- **Paragraph-function sequence:** growth of cloud/edge data processing → programmability of modern network devices → in-network computing opportunity → ML networking workload → reason to run ML in the network → distinction among general, network-assisted, and in-network ML → hardware constraints → survey scope and adjacent surveys → five contributions → organization.
- **Transition mechanisms:** each paragraph reuses the preceding paragraph’s final concept, producing lexical continuity without formulaic connectors; “however” introduces resource limits; a three-way conceptual distinction carries both scope and novelty.
- **Tone and rhythm:** concise, plain, and confident. Short paragraphs create pace, while definitions prevent ambiguity.
- **Related work, gap, contribution, organization:** related work is handled in two sentences: earlier ML/networking and programmable-data-plane surveys supply background but do not cover the intersection. Contributions are short noun-led statements; organization is proportionate.
- **Strong pattern:** another leading exemplar—define the exact conceptual boundary early, state what adjacent surveys cover, and stop once the reader understands the need.
- **Pattern not to imitate:** the generic opening sentence is weaker than the precise conceptual paragraphs that follow.

### COMST_043 — Integrated 5G and time-sensitive networking

- **Paragraph-function sequence:** critical applications and deterministic requirements → limits of current solutions → complementary strengths of TSN and 5G → application-centric survey distinction → cross-domain synthesis → five contributions → brief comparison with existing surveys.
- **Transition mechanisms:** “these domains” turns examples into requirements; “the integration” introduces the solution; “unlike previous surveys” immediately states the differentiator; “we further” raises domain-level observations to cross-domain findings.
- **Tone and rhythm:** very compact and direct, with short paragraphs and minimal historical background. Some generic “comprehensive/foundational” language remains.
- **Related work, gap, contribution, organization:** rather than narrating every prior survey, a comparison table carries most of the evidence. The gap is an application-specific view across four domains with technical mapping. Organization is folded into contribution-to-section references and a figure rather than a separate roadmap paragraph.
- **Strong pattern:** use the comparison table to offload bibliographic detail and keep the Introduction moving.
- **Pattern not to imitate:** contributions appear before the explicit related-survey subsection, and claims of distinctiveness would be stronger if the gap were stated before the list in prose.

### COMST_044 — Integrated sonar and communication

- **Paragraph-function sequence:** platform burden created by separate underwater systems → sonar and communication as historically separate functions → shared bands, components, and processing make integration feasible → application relevance → progression from radar/communication integration to ISAC → relation between IRC and underwater ISC → transferable ideas → underwater physical differences make direct transfer fail → ISC-specific work → absence of a system-level review → contributions → organization.
- **Transition mechanisms:** “nevertheless” turns different performance objectives into shared technical structure; historical progression gives legitimacy; “compared with” and “however” distinguish RF and underwater acoustic regimes; tables make physical differences visible; “while these studies are fundamental” fairly introduces the holistic gap.
- **Tone and rhythm:** technically grounded, comparative, and mostly restrained. Tables absorb complex contrasts, leaving prose to explain why the contrasts matter.
- **Related work, gap, contribution, organization:** component reviews and RF-domain ISAC surveys are separated from a true underwater ISC systems review. The gap is explicitly system-level and medium-specific. Contributions cover synthesis, channel-aware comparison, and metric-based method appraisal; organization is clear.
- **Strong pattern:** the closest rhetorical analogue for O-ISAC in this group—begin with integration pressure, show both commonality and non-transferable physics, and let that duality justify the survey.
- **Pattern not to imitate:** broad “no literature” wording should be replaced by a date-bounded, dimension-specific statement; early military framing may unnecessarily narrow a multi-application field.

### COMST_045 — Intellicise wireless networks from semantic communications

- **Paragraph-function sequence:** post-5G complexity → proposed “intellicise” paradigm → semantic communication as its mechanism → survey focus → related work divided into semantic architectures/applications and AI-plus-wireless → synthesis of each group → relationship and remaining conceptual gap → three large contributions that double as outline → roadmap.
- **Transition mechanisms:** “to this end” introduces the new paradigm and then SemCom; the related-work section uses thematic clustering instead of chronology; synthesis paragraphs connect individual studies to a field-level direction; the contribution section links each claimed contribution directly to a later section.
- **Tone and rhythm:** visionary, abstract, and terminology-heavy. It often favors aspirational concepts over testable engineering statements.
- **Related work, gap, contribution, organization:** prior surveys are grouped by conceptual family and followed by mini-syntheses, a genuine strength. The gap is the relationship between SemCom and the authors’ broader network paradigm. Contributions are long explanatory blocks; organization repeats them.
- **Strong pattern:** summarize what a family of papers collectively establishes before stating what remains unresolved.
- **Pattern not to imitate:** coined terminology, slogans, and claims of self-evolving intelligence can make a survey sound promotional unless tightly operationalized.

### COMST_046 — Metaverse communications, networking, security, and applications

- **Paragraph-function sequence:** term origin and definitions → technology stack → developmental phases → many application and economy examples → social and technical challenges → detailed security/privacy concerns → related surveys across generic, AI, edge, security, and application views → smart-city gap → six contributions → organization.
- **Transition mechanisms:** chronological and categorical accumulation drives most of the text; “however/still” introduce concerns after opportunities; “contrary to” positions the paper against prior survey categories.
- **Tone and rhythm:** expansive, popularizing, and frequently speculative. The Introduction resembles a mini-survey body section and contains numerous illustrative examples.
- **Related work, gap, contribution, organization:** prior surveys are catalogued individually, then contrasted with the paper’s smart-city emphasis. Contributions span networking, blockchain, security, applications, and research directions. Organization is conventional but arrives very late.
- **Strong pattern:** social, governance, and technical risks are treated together rather than presenting the technology as purely beneficial.
- **Pattern not to imitate:** etymology, company examples, cryptocurrency lists, application anecdotes, and long challenge subsections produce a diffuse Introduction; “ground-breaking” and “first” rhetoric further weakens the scholarly voice.

### COMST_047 — MIMO satellite communication systems

- **Paragraph-function sequence:** renewed SatCom interest from lower cost and greater demand → global coverage and standardization → why terrestrial MIMO does not transfer directly → evolving satellite capability → related surveys → two classes of existing coverage → MIMO-specific SatCom focus → section-by-section scope.
- **Transition mechanisms:** two explicitly named drivers give the opening structure; “however” introduces economic change; a second “however” turns MIMO success into SatCom-specific incompatibility; the literature is condensed into two categories before the exact goal is stated.
- **Tone and rhythm:** restrained and compact. The paper avoids a separate inflated contribution list and uses the organization bullets to explain what readers will learn.
- **Related work, gap, contribution, organization:** prior work is divided into general SatCom/NTN surveys and standards-oriented surveys. The gap is PHY-layer MIMO under SatCom constraints. Contributions are implicit in four content blocks rather than advertised with superlatives.
- **Strong pattern:** a survey can establish novelty through a precise focus sentence and a well-structured roadmap without repeatedly claiming comprehensiveness.
- **Pattern not to imitate:** the Introduction could articulate the missing analytical dimensions more explicitly before moving to the roadmap.

### COMST_048 — Multicasting in mmWave and sub-THz systems

- **Paragraph-function sequence:** future high-rate applications → multicasting’s resource benefit and wireless limitation → five directionality-related design challenges → possible technical responses → survey’s two-part scope → closest prior studies → missing modeling and system dimensions → organization.
- **Transition mechanisms:** the general multicast problem is narrowed to mmWave/sub-THz; “if, on one hand/on the other hand” makes directionality a benefit and a cost; sequential challenge paragraphs create controlled accumulation; “some challenges can be alleviated” moves from diagnosis to solution space; “as the main difference” states the survey’s organizing principle.
- **Tone and rhythm:** engineering-focused and analytical. It is detailed, but the details all serve one physical theme: directional transmission.
- **Related work, gap, contribution, organization:** prior works are evaluated against multicasting, high-frequency operation, 5G/6G, and mathematical methodology. The gap is models, methods, and solutions for directional multicast systems. Organization is explicit and concise.
- **Strong pattern:** choose one causal mechanism and let it organize the challenges, prior-work comparison, and survey taxonomy.
- **Pattern not to imitate:** five consecutive challenge paragraphs can feel list-like unless periodically synthesized.

### COMST_049 — Multi-modal foundation models for wireless prediction and control

- **Paragraph-function sequence:** foundation-model definition and value → transformer mechanism and distinctive properties → current small custom models in wireless networks → single-use limitation → network-management complexity → growing modality diversity → cost and reuse rationale → foundation models for prediction and control → distinction from LLMs and generative AI → prior surveys by model family and wireless focus → exact multi-modal prediction/control gap → three contributions → organization.
- **Transition mechanisms:** “however” repeatedly exposes what custom models cannot do; the three limitations escalate from reuse to task complexity to data diversity; “the discussions above” synthesizes them into the FM need; concept comparison prevents fashionable terms from being conflated.
- **Tone and rhythm:** current and technical, with a clear motivation ladder. Some claims about breakthroughs and exceptional capabilities are more promotional than necessary.
- **Related work, gap, contribution, organization:** adjacent LLM, generative-AI, general-FM, and wireless-FM surveys are separated, then the paper’s multi-modal prediction/control focus is stated. Contributions follow exactly those axes and the data/methods needed to build wireless FMs.
- **Strong pattern:** multiple limitations are effective when each adds a nonredundant reason for the same survey scope.
- **Pattern not to imitate:** repeated “comprehensive/in-depth” qualifiers and broad field-shaping claims can be replaced by named coverage dimensions.

### COMST_050 — Industry 5.0 technologies, trends, challenges, and opportunities

- **Paragraph-function sequence:** rhetorical equation and history of industrial revolutions → Industry 4.0/5.0 comparison → human-machine collaboration and many enabling examples → social factory, sensing, 6G, AI, demographics, and transition themes → motivations → need for a survey → research directives → contributions → systematic-review method → related surveys → literature-selection taxonomy → organization and table guide.
- **Transition mechanisms:** primarily chronological and additive; subsection headings, tables, and lists do more organizational work than paragraph-to-paragraph reasoning. Contrast between Industry 4.0 automation and Industry 5.0 human centricity is the recurring link.
- **Tone and rhythm:** highly promotional, conversational in places, and extremely long. Repetition and lists dominate the pacing.
- **Related work, gap, contribution, organization:** prior surveys are compared across technologies, trends, challenges, and opportunities. The gap is breadth across all four. Contributions, methodology, research questions, classification criteria, and table navigation all appear in the Introduction.
- **Strong pattern:** the four analytical dimensions are consistent from prior-work comparison through taxonomy.
- **Pattern not to imitate:** slogan-like opening, sweeping inevitability claims, repeated history, methodology-first emphasis, and excessive navigation. This is a clear negative exemplar for a natural COMST Introduction.

### COMST_051 — Near-field communications

- **Paragraph-function sequence:** 5G impact and next-generation demands → large arrays/high frequencies create a far-to-near-field transition → plane-wave versus spherical-wave physics → quantitative aperture example → extensive history from optics to modern MIMO → prior works grouped as magazines, tutorials, and surveys → specific missing principles, performance limits, tools, and applications → five contributions → organization.
- **Transition mechanisms:** “these objectives necessitate” moves from applications to enabling hardware; “more than a quantitative increase” frames the qualitative change; physics leads into history; “although” and “consequently” convert prior coverage into a survey gap.
- **Tone and rhythm:** authoritative tutorial prose, unusually historical and detailed. Technical precision is high, but the Introduction is close to a self-contained tutorial chapter.
- **Related work, gap, contribution, organization:** source types are explicitly distinguished by purpose—high-level magazine, step-by-step tutorial, and literature survey. The paper then states what a true survey still lacks. Contributions follow physics, modeling, performance, signal processing, and integration.
- **Strong pattern:** distinguish genres of prior work before claiming that a literature survey remains necessary.
- **Pattern not to imitate:** centuries of history before the gap is appropriate only when historical lineage is itself a contribution; otherwise it delays the reader’s arrival at the research problem.

### COMST_052 — Network slicing and learning for Internet of Vehicles

- **Paragraph-function sequence:** smart mobility and broad IoV definition → communication levels and cellular capabilities → 5G/6G requirements and resource challenges → network slicing → machine learning → survey scope as intersections among IoV, slicing, and ML → related surveys for adjacent pairwise intersections → prior work on the exact three-way intersection → comparison taxonomy → contributions → organization.
- **Transition mechanisms:** widening from road vehicles to air and maritime domains justifies the IoV boundary; “all these requirements” introduces slicing; “along with this” introduces ML; a scope diagram and explicit set intersections make the literature gap visible.
- **Tone and rhythm:** descriptive and systematic, but long and definition-heavy. The intersection framing gives coherence to an otherwise broad subject.
- **Related work, gap, contribution, organization:** prior work is grouped by IoV+ML, slicing+ML, slicing+IoT, and IoV+slicing+ML. The gap is full coverage across terrestrial, aerial, and maritime IoV, including datasets, tools, projects, and applications. Contributions and organization directly follow that grid.
- **Strong pattern:** express scope as a defensible intersection of literatures rather than as an ever-expanding topic list.
- **Pattern not to imitate:** long preliminary definitions and paper-by-paper summaries can be compressed once the intersection diagram and comparison table carry the logic.

## Cross-corpus findings

### 1. The common narrative skeleton

The 25 Introductions do **not** share one mandatory template, but the stronger examples repeatedly use the following causal sequence:

1. **Begin with an observable system need or physical fact.** The best openings are not “technology X is growing rapidly.” They explain a concrete condition: deep-space attenuation, a programmable switch, directional high-frequency beams, acoustic propagation, or spherical rather than plane waves.
2. **Introduce the candidate integration or technology as a response.** The response is explained mechanistically, not merely named.
3. **Expose the cost, incompatibility, or unresolved coupling.** Strong Introductions contain an early reversal: reuse is attractive but not free; terrestrial assumptions do not transfer; greater directionality improves link budget but complicates multicast; integration offers sensing but creates security or resource tension.
4. **Define the survey’s conceptual boundary.** This may be a three-way distinction (`COMST_042`), a literature intersection (`COMST_052`), a medium-specific contrast (`COMST_044`), or analytical axes (`COMST_039`).
5. **Position adjacent reviews fairly and dimensionally.** Strong gap statements name what earlier reviews do cover, then identify the missing relation, evidence type, physical regime, measurement basis, or synthesis axis.
6. **State contributions as intellectual operations.** Useful verbs include distinguish, classify, reconcile, compare under conditions, trace mechanisms, and identify limits. “Comprehensively review” alone conveys little.
7. **Close with a proportionate roadmap.** The organization paragraph should confirm the logic already established, not introduce a second contribution list.

This skeleton is causal rather than ceremonial: each stage should make the next stage necessary.

### 2. Transition mechanisms that produce a natural COMST flow

The strongest transitions do not depend on a high count of connector words. They use several deeper mechanisms:

- **Lexical carry-over:** the final concept in one paragraph becomes the subject of the next (`COMST_042`).
- **Benefit-to-cost reversal:** a technology’s enabling property also creates the next design problem (`COMST_033`, `COMST_048`).
- **Generic-to-medium-specific contrast:** a known RF, terrestrial, or far-field solution is tested against a new physical regime (`COMST_036`, `COMST_044`, `COMST_051`).
- **Mechanism-to-evidence move:** a physical explanation is followed by prototype, standards, or deployment evidence (`COMST_028`, `COMST_032`, `COMST_041`).
- **Taxonomic narrowing:** a broad field is separated into adjacent categories until the survey’s exact intersection is visible (`COMST_034`, `COMST_049`, `COMST_052`).
- **Fair concession before gap:** “these works establish X; they do not yet connect X to Y.” This is more credible than declaring prior work inadequate (`COMST_041`, `COMST_044`).
- **Synthesis sentence after accumulation:** after several examples or limitations, a short sentence states what they collectively imply. Strong texts use this reset; weaker texts continue listing.

### 3. Tone and rhythm recipe

The corpus supports a measured technical voice, but it also shows considerable author variation. A defensible COMST-like tone should therefore be learned from the stronger patterns, not from a blind average of everything published.

- Prefer a **calm declarative voice** with claims limited by operating condition, physical regime, or evidence type.
- Alternate **medium explanatory sentences** with occasional short hinge sentences. Uniformly long prose becomes encyclopedic; uniformly short prose becomes staccato.
- Let one paragraph perform one primary rhetorical job, even when it contains several examples.
- Use technical detail where it explains *why* the field needs synthesis. Move exhaustive histories, standards catalogues, and metric inventories to later sections or tables.
- Name tensions directly. Phrases equivalent to “this reuse has a cost” or “the two quantities share a label but not a measurement plane” are more engaging than ornamental importance claims.
- Avoid habitual claims such as “groundbreaking,” “revolutionary,” “unparalleled,” “indispensable,” and “first of its kind” unless the statement is both necessary and auditable.
- Avoid repeating “comprehensive,” “systematic,” and “holistic.” Demonstrate breadth with explicit dimensions.

### 4. Related-work and gap recipe

The most credible gap construction in this group has four parts:

1. Identify two to four **closest survey families**, not every paper in the area.
2. Give each family a fair positive clause describing what it establishes.
3. Compare them on dimensions that the new survey will actually use later: modality, physical regime, architecture, metric definition, validation level, task coupling, or evidence provenance.
4. State the residual gap as a missing **relationship or synthesis operation**, not simply a missing topic.

Comparison tables are useful when they offload detail from prose. They become counterproductive when the prose narrates every cell again. `COMST_041`, `COMST_042`, `COMST_044`, and `COMST_048` are stronger models than the paper-by-paper catalogues in `COMST_028`, `COMST_029`, `COMST_030`, `COMST_046`, and `COMST_050`.

### 5. Contribution and organization recipe

- Contributions should follow directly from the gap and use **non-overlapping operations**. Three to five items are usually sufficient.
- A taxonomy is not automatically a contribution; the contribution is the principle by which the taxonomy makes otherwise incompatible evidence intelligible.
- A comparison is only meaningful when the measurement plane, conditions, baseline, and validation setting remain visible.
- A roadmap should express dependency: foundations enable the comparison framework; the framework structures the evidence synthesis; the synthesis supports discussion and research priorities.
- Avoid repeating contribution bullets verbatim in the organization paragraph.

### 6. Strong exemplars and negative controls within Group B

The strongest prose designs for the present O-ISAC manuscript are:

- **`COMST_041`** for a natural physical-problem → optical-opportunity → residual-limit → fair-gap flow.
- **`COMST_042`** for brevity, conceptual boundary setting, and lexical continuity.
- **`COMST_044`** for explaining why integrated functions are compatible yet why another domain’s methods cannot be transferred without preserving medium-specific physics.
- **`COMST_048`** for organizing an Introduction around one causal mechanism and its trade-offs.
- **`COMST_034`** and **`COMST_052`** for defensible multi-axis/intersection scope.

Useful but intentionally longer tutorial models are `COMST_032`, `COMST_040`, and `COMST_051`. They should inform technical explanation, not the target Introduction length.

Negative controls are equally important. `COMST_028`, `COMST_037`, `COMST_046`, and especially `COMST_050` show that COMST publication does not license catalogue prose, repeated superlatives, slogan-like openings, or an Introduction dominated by method and navigation.

## Group-B recipe for the O-ISAC Introduction

For the new O-ISAC survey, the most appropriate Group-B-derived flow is:

1. Start with the physical fact that a communication-bearing optical field also records interaction with its propagation environment.
2. Turn that fact into the engineering appeal of infrastructure or waveform reuse.
3. Introduce the cost of reuse: shared pilots, power and linearity limits, receiver processing, overhead, and the possibility that one task discards observables needed by the other.
4. Explain why “optical ISAC” is a family of regimes—fiber, FSO/VLC, photonic generation/distribution of RF or THz, and hybrid systems—rather than a single interchangeable platform.
5. Define inclusion broadly enough to cover meaningful coupling, while leaving the strength and location of coupling to the taxonomy.
6. Make comparison validity the central scientific problem: identical labels may refer to different measurement planes, estimator outputs, aggregation scopes, overhead conventions, and implementation states.
7. Position related surveys by what they cover, then identify the missing evidence-governed synthesis across modality, architecture, metric semantics, validation, and communication–sensing trade-offs.
8. State contributions as the operations the survey performs: reconcile the evidence base, classify coupling, preserve metric provenance, compare only under declared conditions, and derive research priorities from validation and reproducibility gaps.
9. End with a short roadmap that follows this logic. Keep PRISMA mechanics in the Methods section; mention them in the Introduction only if needed to support the credibility of the evidence base, not as the paper’s leading contribution.

This recipe is consistent with the strongest narrative practices in the 25-paper group while avoiding imitation of topic-specific wording or sentence structure.

## Coverage conclusion

**Eligible introductions read: 25/25.** `COMST_031` was deliberately excluded as a non-COMST article. No eligible ID in the requested range is missing, and no manuscript file was changed during this audit.
