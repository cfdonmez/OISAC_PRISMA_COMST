

{0}------------------------------------------------

# Perception-Enhanced Multitask Multimodal Semantic Communication for UAV-Assisted Integrated Sensing and Communication System

Ziji Guo† , Haonan Tong† , Zhilong Zhang† , Danpu Liu† †Beijing Key Laboratory of Network System Architecture and Convergence, Beijing Advanced Information Network Laboratory, Beijing University of Posts and Telecommunications, Beijing, China 100876. Email: zijiguo@bupt.edu.cn, hntong@bupt.edu.cn, zhangzhilong@bupt.edu.cn, dpliu@bupt.edu.cn

*Abstract*—Recent advances in integrated sensing and communication (ISAC) unmanned aerial vehicles (UAVs) have enabled their widespread deployment in critical applications such as emergency management. This paper investigates the challenge of efficient multitask multimodal data communication in UAV-assisted ISAC systems, in the considered system model, hyperspectral (HSI) and LiDAR data are collected by UAV-mounted sensors for both target classification and data reconstruction at the terrestrial BS. The limited channel capacity and complex environmental conditions pose significant challenges to effective air-to-ground communication. To tackle this issue, we propose a perceptionenhanced multitask multimodal semantic communication (PE-MMSC) system that strategically leverages the onboard computational and sensing capabilities of UAVs. In particular, we first propose a robust multimodal feature fusion method that adaptively combines HSI and LiDAR semantics while considering channel noise and task requirements. Then the method introduces a perception-enhanced (PE) module incorporating attention mechanisms to perform coarse classification on UAV side, thereby optimizing the attention-based multimodal fusion and transmission. Experimental results demonstrate that the proposed PE-MMSC system achieves 5%–10% higher target classification accuracy compared to conventional systems without PE module, while maintaining comparable data reconstruction quality with acceptable computational overheads.

*Index Terms*—multimodal, semantic communication, unmanned aerial vehicles, multitask, integrated sensing and communication

## I. INTRODUCTION

The emergence of the low-altitude economy has significantly advanced the research of unmanned aerial vehicles (UAVs) in industrial applications [1], particularly in mission critical domains such as disaster response [2]. Modern UAV with advantages of rapid deployment capability, adaptive mission scheduling flexibility, and aerial line-of-sight (LoS) coverage that attributes not only satisfy fundamental communication demands but also enable UAVs to excel in remote sensing operations [3], including precision disaster assessment and dynamic target localization. The increasing complexity of aerial missions now demands concurrent execution of heterogeneous tasks, particularly sensing and communication functions, under constrained computational resources. This operational imperative has driven the development of integrated sensing and communication (ISAC) architectures, which enable unified coordination between multiple tasks [4].

In recent years, ISAC has been extended from traditional millimeter wave radar-based perception to multimodal sensor integration on UAVs, which improves communication performance through sensor collaborations [5]. This evolution has driven growing interest in multimodal fusion within remote sensing [6]. Fusion methods were classified into symmetric approaches (including fusion at the data level, semantic level, and decision level) and asymmetric approaches based on the data hierarchy in [7]. However, the piror arts predominantly treat multimodal data as simple multi-channel inputs, to address these limitations, the scale inconsistency was resolved in [8] across modalities through pyramid structures and multistep fusion networks, while [9] adapted multimodal channel weights according to Line-of-Sight (LoS) conditions. Besides, in many scenarios, it is not sufficient to merely accomplish a single task, rather, multiple tasks need to be completed using remote sensing data. EndNet, proposed in [10], addressed the requirements of multimodal fusion for target classification and data reconstruction. Meanwhile, Image Transmission and Performance Analysis (MTP) in [11] considered the needs of segmentations, image classification, and change detection, as discussed. Unfortunately, existing solutions introduce high computational costs and assume data acquisition and task execution on the same side, neglecting bandwidth constraints and environmental noise impacts on transmission.

The bandwidth limitations and dynamic characteristics of UAV communications have promoted semantic communication as an effective solution [12] [13]. In [14], it was shown that semantic communication can substantially reduce data transmission volumes while maintaining communication robustness under low SNR conditions. To enhance semantic communication reliability in remote sensing field, a guideinspired Transformer block was designed in [15] to build decoders that improve the accuracy of semantic information extraction. Furthermore, a multipath atrous module was proposed in [16] to address progressive semantic segmentation tasks, further advancing the efficiency of semantic communication 

{1}------------------------------------------------

in complex environments. Moreover, multisource multimodal semantic communication has been widely discussed. In [17], a diffusion - model (DM) - based channel enhancer (DMCE) is proposed to extract and compress multi - source data features. In [18], an efficient multimodal data communication scheme for video conferencing is studied, which can effectively compress data while ensuring video transmission quality. Nevertheless, current approaches predominantly utilize raw remote sensing data as what to be transmitted and fused, lacking explicit task-oriented designs and in-depth analysis in multimodal fusion processes.

A perception-enhanced multitask multimodal semantic communication framework for UAV-ISAC networks is studied in this paper. We consider UAVs equipped with multimodal sensors capable of collecting complementary hyperspectral (HSI) and LiDAR remote sensing data. These data are transmitted to the base station (BS), which concurrently executes two mission-critical tasks: target classification and data reconstruction. Building upon the synergistic design of ISAC, we propose to exploit the UAV's inherent sensing capabilities to optimize semantic information fusion and transmission efficiency. The principal contributions of this work are as follows:

- A perception-enhanced multitask multimodal semantic communication (PE-MMSC) framework for UAV-assisted ISAC is proposed. In multitask scenarios, we consider the limited computational power of UAVs, and introduce a Perception Enhancement (PE) module on the UAV side, which is a lightweight neural network, to enhance the performance of multitask.
- We design a specific PE module with an attention mechanism. The PE module performs preliminary coarse classification on the UAV side to provide an interference-free classification result as a reference, thereby adjusting the channel attention in the multimodal fusion process.
- The proposed framework is tested on a real-world remote sensing dataset. The results demonstrate that the PE-MMSC system achieves significant performance improvements with minimal computational cost. The target classification accuracy is improved by 5% to 10% while ensuring data reconstruction quality compared to traditional system without PE module.

#### II. SYSTEM MODEL

#### A. System Architecture

We investigate a scenario where UAV collaborate with BS to accomplish multitask. To achieve comprehensive environmental perception and ensure task quality under low SNR levels, the UAV equipped with multimodal sensors extracts semantic features from the sensing data, fuses them and transmit to the BS. In practical applications, different tasks necessitate diverse requirements, BS is required to perform multitasking with fused data, including target classification and data reconstruction, as illustrated in Fig.1.

Taking into account the distinct emphases that different remote sensing modalities place on characterizing the environment, we chose HSI data  $D^{\rm HSI}$  and LiDAR data  $D^{\rm LiDAR}$  as sensing data.  $D^{\rm HSI}$  contains 2D data from multiple frequency range, while  $D^{\rm LiDAR}$  provides 3D spatial information. In addition, the semantic extraction and fusion techniques employed reduce information redundancy between modalities, thus decreasing the amount of transmitted data, which is particularly beneficial in UAV communication scenarios constrained by limited bandwidth.

Semantic communication is used to against the channel noise and fading, ensuring transmission quality even under low SNR levels, which including PE-MMSC framework and PE module. Next we will introduce them.

The proposed PE-MMSC framework addresses the multitask demands of the BS in complex scenarios, while the PE Module on the UAV. This compensates for the lack of effective fusion guidance in traditional multimodal fusion methods at the semantic level, enabling effective adjustment of channel attention during the semantic fusion processes. The PE module on the UAV side performs outputs preliminary coarse classification result  $C^{\rm pre}$  to guide the multimodal fusion. Due to its immunity to environmental interference,  $C^{\rm pre}$  offers valuable classification information, enhancing the UAV to refine the effective information under low SNR levels.

## B. Semantic Fusion and Communication Model

Since  $D^{\text{LiDAR}}$  mainly contain spatial information, which performs less relativity with target classification task, here, we take  $D^{\text{HSI}}$  as the primary modality, with  $D^{\text{LiDAR}}$  serving as the auxiliary modality.  $D^{\text{HSI}}$  and  $D^{\text{LiDAR}}$  are first processed through an semantic encoder to extract the semantic features, given by

$$S^{\text{mod}} = f_{\omega^{\text{mod}}}^{\text{E}}(\boldsymbol{D}^{\text{mod}}), \text{ mod } \in \{\text{HSI,LiDAR}\}$$
 (1)

where  $f_{\varphi^{\mathrm{mod}}}^{\mathrm{E}}(\cdot)$  represents the encoder function parameterized by  $\varphi_{\mathrm{E}}^{\mathrm{mod}}$ , and  $\mathbf{S}^{\mathrm{mod}} = [s_1^{\mathrm{mod}}, ..., s_{n^{\mathrm{mod}}}^{\mathrm{mod}}]$  represents the extracted semantic features of different modality with  $n^{\mathrm{mod}}$  is the feature number, and  $s_{i^{\mathrm{mod}}}$  for the i-th semantic feature of different modality. Furthermore,  $\mathbf{S}^{\mathrm{HSI}}$  is employed on the UAV to perform preliminary coarse classification, which is given by

$$\boldsymbol{C}^{\text{pre}} = f_{y_{\text{pre}}}^{\text{C}}(\boldsymbol{S}^{\text{mod}}) \tag{2}$$

where  $C^{\rm pre}=[p_1^{\rm pre},...,p_m^{\rm pre}]$  represents the preliminary coarse classification result with pre means preliminary, m is the number of target categories, which contributes to subsequent multimodal fusion, and  $p_i^{\rm pre}$  for the classification probability of i-th categories.  $f_{\psi pre}^{\rm C}$  represents the preliminary coarse classification function parameterized by  $\psi^{\rm pre}$ . Subsequently, all single-modal semantic features are fused under the guidance of  $C^{\rm pre}$  to obtain multimodal fusion semantic features as

$$S = f_{\omega}^{F}(S^{\text{HSI}}, S^{\text{LiDAR}}, C^{\text{pre}})$$
 (3)

where  $f_{\omega}^F(\cdot)$  represents the fusion function parameterized by  $\omega$ , and  $\boldsymbol{S}$  is the fused semantic features. Then,  $\boldsymbol{S}$  is transmitted via a wireless channel as

$$\hat{\boldsymbol{S}} = h \cdot \boldsymbol{S} + \boldsymbol{n} \tag{4}$$

{2}------------------------------------------------

![](_page_2_Figure_1.jpeg)

Fig. 1: Perception-enhanced multitask multimodal semantic communication for UAV-assisted ISAC system

where  $\hat{S}$  represents the semantic features received by the BS after transmission degradation, h is Rayleigh channel coefficient [19], and  $n \sim \mathcal{N}(0, \sigma^2 I)$  denotes Gaussian channel noise with  $\sigma^2$  being noise variance and I being identity matrix.

BS utilizes  $\hat{S}$  to perform multiple tasks, including data reconstruction and target classification. The data reconstruction is

$$\hat{\boldsymbol{D}}^{\text{mod}} = f_{\varphi_D^{\text{mod}}}^{\text{D}}(\hat{\boldsymbol{S}}) \tag{5}$$

where  $f_{\varphi_D^{\mathrm{mod}}}^{\mathrm{D}}(\cdot)$  represents the decoder function parameterized by  $\varphi_D^{\mathrm{mod}}$ , and  $\hat{D}^{\mathrm{mod}}$  denotes the sensing reconstructed from the corresponding modality. Target classification is

$$\boldsymbol{C}^{\text{fin}} = f_{\eta/\text{fin}}^{\text{C}}(\hat{\boldsymbol{S}}) \tag{6}$$

where  $f_{\psi^{\rm fin}}^{\rm C}(\cdot)$  represents the multimodal target classification function parameterized by  $\psi^{\rm fin}$ , and  $C^{\rm fin}$  denotes the final classification result with fin means final.

We consider transmitting N samples, getting sensing data  $\mathbf{D}_N^{\mathrm{mod}} \in \mathbb{R}^{N \times n^{\mathrm{mod}}}$  in UAV, and finally output data reconstruction results  $\hat{\mathbf{D}}_N^{\mathrm{mod}} \in \mathbb{R}^{N \times n^{\mathrm{mod}}}$  and target classification result  $\mathbf{C}_N^{\mathrm{phase}} \in \mathbb{R}^{N \times m}$ , with phase  $\in \{\mathrm{pre}, \mathrm{fin}\}$  to represent the classification phase. For the data reconstruction, we use Normalized Mean Squared Error(NMSE) as an evaluation metric, which is given by

$$NMSE(\boldsymbol{D}_{N}^{mod}, \hat{\boldsymbol{D}}_{N}^{mod}) = \frac{\mathbb{E}\left[\left\|\boldsymbol{D}_{N}^{mod} - \hat{\boldsymbol{D}}_{N}^{mod}\right\|^{2}\right]}{\mathbb{E}\left[\left\|\boldsymbol{D}_{N}^{mod}\right\|^{2}\right]}$$
(7)

where  $\mathbb{E}(\cdot)$  represents expected value function, and  $A(\cdot,\cdot)$  is used to evaluate target classification, given by

$$A(\boldsymbol{C}_{N}^{\text{fin}}, \boldsymbol{C}_{N}^{\text{true}}) = \mathbb{E}[\mathbb{I}[\operatorname{argmax}(\boldsymbol{C}_{N}^{\text{fin}}) = \operatorname{argmax}(\boldsymbol{C}_{N}^{\text{true}})]]$$
(8)

where argmax means argument of the maximum,  $\boldsymbol{C}_N^{\text{true}}$  represents ground truth samples, shaped in one-hot format.

$$\mathbb{I}[x] = \begin{cases} 1, & \text{if } x \text{ is true} \\ 0, & \text{if } x \text{ is false} \end{cases}$$
(9)

In this paper, we place particular emphasis on the performance aspects of target classification. Therefore, the goal of the PE-MMSC system is to maximize the accuracy of target

classification while ensuring the quality of data reconstruction via optimize the codec parameters. The system objective is:

$$\max_{\psi,\varphi,\omega} A(\boldsymbol{C}_N^{\text{fin}}, \boldsymbol{C}_N^{\text{true}}) \tag{10a}$$

s.t. 
$$\text{NMSE}(\boldsymbol{D}_{N}^{\text{mod}}, \hat{\boldsymbol{D}}_{N}^{\text{mod}}) \leq \beta, \ \forall \text{mod}$$
 (10b)

where , with  $\beta$  represents the The threshold of NMSE for data reconstruction. Owing to the complex data manifold of the sensing data, we propose employing a neural network (NN) based model to optimize the parameters and implement the functions.

#### III. PE-MMSC DESIGN

In this section, a detailed design of the PE-MMSC is presented. Specifically, we focus on the fusion of multimodal semantics by the guidance of PE module with attention mechanism.

## A. Perception Enhanced Module

The PE module is introduced in this section. In contrast to traditional semantic fusion approaches, where  $S^{\rm HSI}$  and  $S^{\rm HSI}$  are merely concatenated and input into the fusion module, we propose to input  $C^{\rm pre}$  into the semantic fusion encoder. This serves as a guidance for the attention weight adjustment of each modality, as depicted in Fig. 2, the intensity of  $C^{\rm pre}$  reflects the prediction probabilities for each category, with red lines indicating enhanced semantic feature weights and blue lines indicating reduced semantic feature weights. The

![](_page_2_Picture_24.jpeg)

Fig. 2: Attention mechanism of perception enhanced fusion

attention mechanism of it, is  $C^{\text{pre}}$  provides an unbiased coarse classification probability distribution during the semantic fusion stage,  $C^{\text{pre}}$  plays a role in stage-wise supervision, effectively guiding the allocation of feature weights in the fusion process.

{3}------------------------------------------------

WS21 IEEE ICC 2025 Workshop on Integrated Sensing and Communications for Low-Altitude Intelligent Network During continuous training stage, the NN identifies semantic fusion encoder fuses the complementary characteristics and seelements correlated with the max classification probability  $p_{\text{max}}^{\text{pre}}$ and strengthens their weights through binding mechanisms. Conversely, semantic elements related to min classification probability  $p_{\min}^{\text{pre}}$  undergo weight reduction. This dynamic adjustment mechanism optimizes attention weights, ensuring that features strongly correlated with the primary classification obtain increased focus, thereby improving overall classification performance.

 $C^{\mathrm{pre}}$  provides the fusion guidance that is lacking in traditional multimodal fusion. This enables the fusion process to not solely rely on the self-adjustment of NNs, but rather to purposefully assign greater weights to more important semantic features based on the preliminary coarse classification result  $[p_1^{\text{pre}},...,p_m^{\text{pre}}]$ . Consequently, under the same SNR, the proportion of important information is increased, which enhances the robustness against noise and channel fading, thereby improving the overall task performance.

In summary, the role of PE-module in the semantic fusion process can be outlined in the following aspects:

- Guiding feature selection:  $C^{\text{pre}}$  enables the semantic fusion encoder to selectively strengthen the most relevant features to the task, while suppressing irrelevant features.
- Improving fusion efficiency: by visualizing the weight changes of  $C^{\text{pre}}$  during the fusion process, researchers can gain a more intuitive understanding of the modality fusion between  $S^{HSI}$  and  $S^{LiDAR}$ , which enhance the effectiveness of feature fusion.

#### B. Semantic Codec

The NN architectures of the various semantic codecs are introduced in this section, including the semantic encoder, classifier, fusion encoder, and decoder, as well as the design of their respective loss functions.

- 1) Semantic Encoder: an encoder based on the ReLU Block (RB) is utilized to extract  $S^{\text{mod}}$  from  $D^{\text{mod}}$ . Each RB comprises an FC layer, a BN layer, and a ReLU activation function. Through multiple RB structures, the semantic encoder can gradually extract semantic features at varying levels.
- 2) Classifier: to alieviate the computational of UAV, a single FC layer is employed to perform  $f_{\psi^{\text{pre}}}^{\text{C}}(\cdot)$ . For consistency in the PE-MMSC, the same layer is adopted for  $f_{\scriptscriptstyle{\eta/\mathrm{fin}}}^{\mathrm{C}}(\cdot)$  at BS. The loss function of target classification module is cross entropy function, given by

$$L_{\psi,\varphi,\omega}(\boldsymbol{C}_{N}^{\text{phase}},\boldsymbol{C}_{N}^{\text{true}}) = -\frac{1}{N} \sum_{i=1}^{N} \sum_{j=1}^{m} C_{i,j}^{\text{true}} log(C_{i,j}^{\text{phase}}) \quad (11)$$

where  $C_{i,j}^{\text{true}}$  and  $C_{i,j}^{\text{phase}}$  are the elements at the i-th row and j-th column of  $C_N^{\text{true}}$  and  $C_N^{\text{phase}}$ .

3) Semantic Fusion Encoder: the structure of the semantic fusion encoder is similar to that of the encoder, but it requires fewer RBs because its primary function is to perform the fusion of semantic features rather than their extraction. The semantic

mantic redundancy between different modalities, and attention mechanism of PE is employed to enhance the fusion process.

4) Semantic Decoder: the decoder is constructed based on the Sigmoid Block (SB) and is designed to reconstruct  $D^{\text{mod}}$ . It similarly incorporates an FC and BN layer; however, the activation function is replaced by a sigmoid function. This modification is because the Sigmoid function confines the output within the range of 0 and 1, which is beneficial for constraining the output range in data reconstruction tasks. For data reconstruction, the mean squared error (MSE) loss function is employed, gievn by

$$L_{\psi,\varphi,\omega}(\boldsymbol{D}_{N}^{\text{mod}},\hat{\boldsymbol{D}}_{N}^{\text{mod}}) = \left\|\boldsymbol{D}_{N}^{\text{mod}} - \hat{\boldsymbol{D}}_{N}^{\text{mod}}\right\|^{2}$$
(12)

We modify the traditional multimodal semantic fusion framework by changing the NN layer in [10], adding a PE module, and wireless channel training. A detailed description of each module's NN layers is provided in Table I.

## **Algorithm 1** Training algorithm of PE-MMSC

- 1: Initialization: Deploy a neural network and set up channels. Initialize the model parameters of  $\psi$ ,  $\varphi$ ,  $\omega$ .
- 2: for iteration of epoch do do
- for each batch of training data do do
- **Multimodal Sensing:** get data  $m{D}_N^{\mathrm{HSI}}$  and  $m{D}_N^{\mathrm{LiDAR}}$  from training batches.
- Semantic Extraction: input  $D_N^{\rm HSI}$ ,  $D_N^{\rm LiDAR}$ , output  $S_N^{\rm HSI}$ ,  $S_N^{\rm LiDAR}$ . Perception Ehanced: 5:
- 6:
  - input  $S_N^{\mathrm{HSI}}$ , output  $C_N^{\mathrm{pre}}$ .
- 7:

input 
$$C_{N}^{\text{pre}}$$
  $S_{N}^{\text{HSI}}$   $S_{N}^{\text{LiDAR}}$  output  $S_{N}$ 

- Semantic Fusion: input  $C_N^{\text{pre}}$ ,  $S_N^{\text{HSI}}$ ,  $S_N^{\text{LiDAR}}$ , output  $S_N$ Transmit  $S_N$  through channel and BS receive  $\hat{S}_N$ . 8:
- **Target Classification:** 
  - input  $\hat{S}_N$ , output  $C_N^{\mathrm{fin}}$
- 10:

Data Reconstruction: input 
$$\hat{S}_N$$
, output  $\hat{D}_N^{\mathrm{HSI}}$ ,  $\hat{D}_N^{\mathrm{LiDAR}}$ 

11:

$$L_{\psi,arphi,\omega}(oldsymbol{C}_N^{ ext{pre}},oldsymbol{C}_N^{ ext{fin}},oldsymbol{C}_N^{ ext{HSI}},oldsymbol{\hat{D}}_N^{ ext{HSI}},oldsymbol{\hat{D}}_N^{ ext{LiDAR}},oldsymbol{\hat{D}}_N^{ ext{LiDAR}})$$

- Backpropagation and gradient descent, update the 12: parameters  $\psi$ ,  $\varphi$ ,  $\omega$ .
- 13: end for
- 14: **end for**

#### C. Training and Loss

In conjunction with the optimization objectives (10a) and constraint (10b), we formulate a joint training loss function, given by

$$L_{\psi,\varphi,\omega}(\boldsymbol{C}_{N}^{\text{pre}},\boldsymbol{C}_{N}^{\text{fin}},\boldsymbol{D}_{N}^{\text{HSI}},\hat{\boldsymbol{D}}_{N}^{\text{HSI}},\boldsymbol{D}_{N}^{\text{LiDAR}},\hat{\boldsymbol{D}}_{N}^{\text{LiDAR}},\hat{\boldsymbol{D}}_{N}^{\text{LiDAR}})$$

$$=\alpha_{1}L_{\psi,\varphi,\omega}(\boldsymbol{C}_{N}^{\text{pre}},\boldsymbol{C}_{N}^{\text{true}})+\alpha_{2}L_{\psi,\varphi,\omega}(\boldsymbol{C}_{N}^{\text{fin}},\boldsymbol{C}_{N}^{\text{true}})$$

$$+\alpha_{3}L_{\psi,\varphi,\omega}(\boldsymbol{D}_{N}^{\text{HSI}},\hat{\boldsymbol{D}}_{N}^{\text{HSI}})+\alpha_{4}L_{\psi,\varphi,\omega}(\boldsymbol{D}_{N}^{\text{LiDAR}},\hat{\boldsymbol{D}}_{N}^{\text{LiDAR}})$$

$$(13)$$

{4}------------------------------------------------

where α<sup>i</sup> represents the weight of different tasks, 0 ≤ α<sup>i</sup> ≤ 1.

We opt to jointly train two classifiers and two decoders with the wireless channel. This approach not only enhances the NN's capability to acquire classification information but also ensures that the semantic features ultimately transmitted are not only robust against fading, but also tailored for multi-task robustness. Algorithm 1 outlines the training process, which encompasses parameter initialization, network construction, extraction and fusion of semantic information, transmission of semantic features through the channel, reception and processing of information, calculation of the loss function and parameter updates through backpropagation and gradient descent.

TABLE I: Module NN description

| Module         | Structure                |  |  |  |
|----------------|--------------------------|--|--|--|
| RB block       | FC + BatchNorm + ReLU    |  |  |  |
| SB block       | FC + BatchNorm + Sigmoid |  |  |  |
| Encoder        | 4 RB block               |  |  |  |
| Decoder        | 2 SB block + FC          |  |  |  |
| Fusion Encoder | 2 RB block               |  |  |  |
| Classifier     | FC                       |  |  |  |

## IV. EXPERIMENTS AND ANALYSIS

## *A. Dataset Description*

This study used the Houston2013 dataset [10], which is widely used for performance evaluation in the field of remote sensing and has high-level qualitative and quantitative analytical value. The dataset integrates HSI and LiDAR technologies, covering a spectral range from 364 to 1,046 nanometers. The HSI data comprises 144 bands, while the LiDAR data consists of 349 bands and 1,905 pixels. The samples in the data set are annotated into 15 categories, including various scenes such as forests, water bodies, railways, etc., with each sample representing a pixel point.

## *B. Experimental Setup*

The proposed method is compared with the following baseline approaches:

- Traditional Multimodal Semantic Fusion Algorithm: The EndNet network presented in [10] is used as the reference. The proposed PE-MMSC has more a PE module than the baseline line.
- Deep EndNet: To validate that the performance improvement of the proposed method is due to the attention adjustment enabled by the PE module, rather than a deeper network architecture, we compared it with an EndNet network with a deepened semantic fusion encoder.
- Single-modal Object Classification Algorithm: To assess the generalization capability of the proposed perceptionenhanced design, we also compared the performance of networks with and without the PE module in a singlemodal classification task.

All simulation methods strictly follow the system framework illustrated in Figure 1. Additionally, the NN layer structure used is consistent with the hierarchical configuration listed in Table I. However, in the joint encoder section, the deep network structure introduces additional RB to enhance the feature representation capability. For different simulation schemes, the required floating-point operations are computed according to the methodology described in [19] and detailed in Table II.

TABLE II: The Flops of various simulation methods

| Module and<br>Neural Network | HSI   | LiDAR | PE   | Fusion | Total  |
|------------------------------|-------|-------|------|--------|--------|
| PE-MMSC                      | 13536 | 11568 | 1920 | 43264  | 70288  |
| EndNet                       | 13536 | 11568 |      | 41344  | 66448  |
| DeepEndNet                   | 13536 | 11568 |      | 107136 | 132240 |
| Hsi+PE                       | 13536 |       | 1920 | 26880  | 42336  |
| LiDAR+PE                     |       | 11568 | 1920 | 26880  | 40368  |
| HSI                          | 13536 |       |      |        | 13536  |
| LiDAR                        |       | 11568 |      |        | 11568  |

During the training process, the Adam optimizer is used, with a learning rate of 0.001, a batch size of 64, and a regularization parameter set to α = [0.6, 1, 1, 1]. A total of 600 iterations are executed. Regarding channel modeling, this study utilizes a Rayleigh fading channel with K = 12 for simulation experiments. Furthermore, to ensure semantic consistency across all schemes, all configurations are set to output semantic symbols K = 64.

## *C. Performance Evaluation And Analysis*

Fig. 3-6 illustrate the performance of various simulation methods in the target classification and data reconstruction task under Rayleigh fading channels with different SNR conditions.

Fig. 3 shows that, the proposed PE-MMSC demonstrates a performance improvement of 5% to 10% compared to other methods across different SNR conditions. Notably, the performance enhancement is more significant under low SNR conditions, as the classification information retained in Cpre provides a more direct and valuable guidance, mitigating the impact of noise. Merely increasing the depth of NN, as seen in DeepEndNet, does not achieve the desired improvement

Fig. 4 further validates the generalizability of the proposed PE module. In classification tasks utilizing single-modal data, the PE module also exhibits significant performance improvements, with maximum gains of 3% and 7% for the HSI and LiDAR data, respectively.

Fig. 5 and 6 show the performance of PE-MMSC in data reconstruction tasks. Particularly for LiDAR data reconstruction, the proposed method achieves a maximum reduction in NMSE by 36% compared to EndNet.

We also evaluate the performance of the PE-MMSC system under different numbers of semantic symbols K, as illustrated in Fig. 7. This suggests that K = 64 is sufficient to represent semantic information. This reveals a larger K values are required to improve noise resistance at low SNR levels, whereas smaller K values can be adopted to optimize efficiency at high SNR levels.

A comprehensive analysis of Table II reveals that the proposed PE-MMSC method associated computational overhead is bearable, while the performance gain remains substantial. Table II shows underscores the effectiveness of the proposed

{5}------------------------------------------------

![](_page_5_Figure_1.jpeg)

Fig. 5: NMSE vs SNR (HSI)

Fig. 6: NMSE vs SNR (LiDAR)

![](_page_5_Figure_4.jpeg)

Fig. 7: Different K for Accuracy (PE-MMSC)

method in balancing computational complexity and task performance.

### V. CONCLUSION

In this paper, we investigates an efficient PE-MMSC system for ISAC UAVs. In our considered system, we extract and fusion the semantic features of sensing data. The use of the PE module effectively adjusts the attention during the multimodal semantic fusion process, thereby enhancing performance in multitask scenarios. Simulation results demonstrate that the proposed PE-MMSC significantly improves classification accuracy by 5% to 10% with only a minimal additional computational overhead, while ensuring data reconstruction quality.

## VI. FUNDING

This work is supported in part by the National Natural Science Foundation of China under Grant 62271065 and U22B2001, and Beijing Natural Science Foundation under L242084.

# REFERENCES

 H. Yang, M. Zheng, Z. Shao, Y. Jiang, and Z. Xiong, "Intelligent computation offloading and trajectory planning for 3d target search in low-altitude economy scenarios," *IEEE Wireless Communications Letters*, pp. 1–1, 2025.

- [2] B. Hazarika, P. Singh, K. Singh, S. L. Cotton, H. Shin, O. A. Dobre, and T. Q. Duong, "Generative ai-augmented graph reinforcement learning for adaptive uav swarm optimization," *IEEE Internet of Things Journal*, pp. 1–1, 2025.
- [3] Z. Xiao, L. Zhu, Y. Liu, P. Yi, R. Zhang, X.-G. Xia, and R. Schober, "A survey on millimeter-wave beamforming enabled uav communications and networking," *IEEE Communications Surveys & Tutorials*, vol. 24, no. 1, pp. 557–610, 2022.
- [4] C. Deng, X. Fang, and X. Wang, "Beamforming design and trajectory optimization for uav-empowered adaptable integrated sensing and communication," *IEEE Transactions on Wireless Communications*, vol. 22, no. 11, pp. 8512–8526, 2023.
- [5] X. Cheng, H. Zhang, J. Zhang, S. Gao, S. Li, Z. Huang, L. Bai, Z. Yang, X. Zheng, and L. Yang, "Intelligent multi-modal sensingcommunication integration: Synesthesia of machines," 2023. [Online]. Available: https://arxiv.org/abs/2306.14143
- [6] C. Shi, G. Lai, Y. Yu, M. Bellone, and V. Lippiello, "Real-time multi-modal active vision for object detection on uavs equipped with limited field of view lidar and camera," *IEEE Robotics and Automation Letters*, vol. 8, no. 10, pp. 6571–6578, 2023.
- [7] C. Xiang, C. Feng, X. Xie, B. Shi, H. Lu, Y. Lv, M. Yang, and Z. Niu, "Multi-sensor fusion and cooperative perception for autonomous driving: A review," *IEEE Intelligent Transportation Systems Magazine*, vol. 15, no. 5, pp. 36–58, 2023.
- [8] Y. Sun, Z. Fu, C. Sun, Y. Hu, and S. Zhang, "Deep multimodal fusion network for semantic segmentation using remote sensing image and lidar data," *IEEE Transactions on Geoscience and Remote Sensing*, vol. 60, pp. 1–18, 2022.
- [9] D. Roy, Y. Li, T. Jian, P. Tian, K. Chowdhury, and S. Ioannidis, "Multi-modality sensing and data fusion for multi-vehicle detection," *IEEE Transactions on Multimedia*, vol. 25, pp. 2280–2295, 2023.
- [10] D. Hong, L. Gao, R. Hang, B. Zhang, and J. Chanussot, "Deep encoder-decoder networks for classification of hyperspectral and lidar data," IEEE Geoscience and Remote Sensing Letters, vol. 19, pp. 1–5, 2022.
- [11] D. Wang, J. Zhang, M. Xu, L. Liu, D. Wang, E. Gao, C. Han, H. Guo, B. Du, D. Tao, and L. Zhang, "Mtp: Advancing remote sensing foundation model via multitask pretraining," *IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing*, vol. 17, pp. 11632–11654, 2024.
- [12] J. Kang, H. Du, Z. Li, Z. Xiong, S. Ma, D. Niyato, and Y. Li, "Personalized saliency in task-oriented semantic communications: Image transmission and performance analysis," *IEEE Journal on Selected Areas* in Communications, vol. 41, no. 1, pp. 186–201, 2023.
- [13] H. Tong, Z. Yang, S. Wang, Y. Hu, W. Saad, and C. Yin, "Federated learning based audio semantic communication over wireless networks," in 2021 IEEE Global Communications Conference (GLOBECOM), 2021, pp. 1–6.
- [14] H. Xie, Z. Qin, G. Y. Li, and B.-H. Juang, "Deep learning enabled semantic communication systems," *IEEE Transactions on Signal Processing*, vol. 69, pp. 2663–2675, 2021.
- [15] X. Meng, Y. Yang, L. Wang, T. Wang, R. Li, and C. Zhang, "Class-guided swin transformer for semantic segmentation of remote sensing imagery," *IEEE Geoscience and Remote Sensing Letters*, vol. 19, pp. 1–5, 2022.
- [16] S. Pan, Y. Tao, C. Nie, and Y. Chong, "Pegnet: Progressive edge guidance network for semantic segmentation of remote sensing images," *IEEE Geoscience and Remote Sensing Letters*, vol. 18, pp. 637–641, 2021. [Online]. Available: https://api.semanticscholar.org/CorpusID:219035762
- [17] Y. Zeng, X. He, X. Chen, H. Tong, Z. Yang, Y. Guo, and J. Hao, "Dmce: Diffusion model channel enhancer for multi-user semantic communication systems," in *ICC 2024 - IEEE International Conference on Communications*, 2024, pp. 855–860.
- [18] H. Tong, H. Li, H. Du, Z. Yang, C. Yin, and D. Niyato, "Multimodal semantic communication for generative audio-driven video conferencing," *IEEE Wireless Communications Letters*, vol. 14, no. 1, pp. 93–97, 2025.
- [19] C. You and R. Zhang, "3d trajectory optimization in rician fading for uav-enabled data harvesting," *IEEE Transactions on Wireless Communi*cations, vol. 18, no. 6, pp. 3192–3207, 2019.