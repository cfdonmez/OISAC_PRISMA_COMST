

{0}------------------------------------------------

# SDOA-Net: An Efficient Deep-Learning-Based DOA Estimation Network for Imperfect Array

Peng Che[n](https://orcid.org/0000-0002-7120-1577) , *Senior Member, IEEE*, Zhimin Che[n](https://orcid.org/0000-0001-8477-3163) , *Member, IEEE*, Liang Liu [,](https://orcid.org/0000-0002-6509-9609) *Senior Member, IEEE*, Yun Chen [,](https://orcid.org/0000-0002-3736-9456) *Senior Member, IEEE*, and Xianbin Wan[g](https://orcid.org/0000-0003-4890-0748) , *Fellow, IEEE*

*Abstract*— The estimation of direction of arrival (DOA) is a crucial issue in conventional radar, wireless communication, and integrated sensing and communication (ISAC) systems. However, low-cost systems often suffer from imperfect factors, such as antenna position perturbations, mutual coupling effect, inconsistent gains/phases, and nonlinear amplifier effect, which can significantly degrade the performance of DOA estimation. This article proposes a DOA estimation method named super-resolution DOA network (SDOA-Net) based on deep learning (DL) to characterize the realistic array more accurately. Unlike existing DL-based DOA methods, SDOA-Net uses sampled received signals instead of covariance matrices as input to extract data features. Furthermore, SDOA-Net produces a vector that is independent of the DOA of the targets but can be used to estimate their spatial spectrum. Consequently, the same training network can be applied to any number of targets, reducing the complexity of implementation. The proposed SDOA-Net with a low-dimension network structure also converges faster than existing DL-based methods. The simulation results demonstrate that SDOA-Net outperforms existing DOA estimation methods for imperfect arrays. The SDOA-Net code is available online at https://github.com/chenpengseu/SDOA-Net.git.

Manuscript received 5 January 2024; revised 5 March 2024; accepted 19 March 2024. Date of publication 19 April 2024; date of current version 3 May 2024. This work was supported in part by the Natural Science Foundation for Excellent Young Scholars of Jiangsu Province under Grant BK20220128, in part by the Natural Science Foundation of Shanghai under Grant 22ZR1425200, in part by the Open Fund of State Key Laboratory of Integrated Chips and Systems under Grant SKLICS-K202305, in part by the National Key Research and Development Program of China under Grant 2019YFE0120700, in part by the Open Fund of National Key Laboratory of Wireless Communications Foundation under Grant IFN20230105, in part by the Open Fund of National Key Laboratory on Electromagnetic Environmental Effects and Electro-Optical Engineering under Grant JCKYS2023LD6, in part by the Open Fund of ISN State Key Laboratory under Grant ISN24-04, and in part by the National Natural Science Foundation of China under Grant 61801112. The Associate Editor coordinating the review process was Dr. Takuma Watanabe. *(Corresponding author: Zhimin Chen.)*

Peng Chen is with the State Key Laboratory of Millimeter Waves, Southeast University, Nanjing 210096, China, and also with the State Key Laboratory of Integrated Chips and Systems, Fudan University, Shanghai 201203, China (e-mail: chenpengseu@seu.edu.cn).

Zhimin Chen is with the School of Electronic and Information, Shanghai Dianji University, Shanghai 201306, China, and also with the Department of Electronic and Information Engineering, The Hong Kong Polytechnic University, Hong Kong (e-mail: chenzm@sdju.edu.cn).

Liang Liu is with the Department of Electronic and Information Engineering, The Hong Kong Polytechnic University, Hong Kong (e-mail: liang-eie.liu@polyu.edu.hk).

Yun Chen is with the State Key Laboratory of Integrated Chips and Systems and the Microelectronics School, Fudan University, Shanghai 201203, China (e-mail: chenyun@fudan.edu.cn).

Xianbin Wang is with the Department of Electrical and Computer Engineering, Western University, London, ON N6A 5B9, Canada (e-mail: xianbin.wang@uwo.ca).

Digital Object Identifier 10.1109/TIM.2024.3391338

*Index Terms*— Convolution layer, deep learning (DL), direction of arrival (DOA) estimation, imperfect array, super-resolution method.

### <span id="page-0-1"></span><span id="page-0-0"></span>I. INTRODUCTION

D IRECTION-OF-ARRIVAL (DOA) estimation is a fundamental problem in wireless communications, radar-based applications, and future integrated sensing and communication (ISAC) systems [\[1\],](#page-9-0) [\[2\],](#page-9-1) [\[3\],](#page-9-2) [\[4\]](#page-9-3) and has been studied for decades. Typically, the DOA estimation is based on an ideal antenna array model, without considering any imperfect effect, including the mutual coupling effect, inconsistent gains/phases, nonlinear effect, and so on. In this ideal scenario, DOA can be estimated by traditional methods such as the monopulse angle estimation method [5] [an](#page-9-4)d fast Fourier transformation (FFT)-based methods.

<span id="page-0-4"></span><span id="page-0-3"></span><span id="page-0-2"></span>In addition, there have been proposals for super-resolution estimation methods. Subspace-based methods, such as multiple signal classification (MUSIC) [\[6\],](#page-9-5) [\[7\],](#page-9-6) [\[8\]](#page-9-7) and estimation of signal parameters via rotational invariance techniques (ESPRIT) [\[9\],](#page-9-8) [\[10\],](#page-9-9) [\[11\],](#page-9-10) [\[12\], h](#page-9-11)ave been suggested. An optimization problem is formulated in [\[13\]](#page-9-12) to estimate the DOA considering the eigenvalues ranking problem. In addition, sparse reconstruction-based methods have been introduced that take advantage of the sparsity of signals in the spatial domain. For example, compressed sensing (CS)-based methods have been proposed for DOA estimation, including sparse Bayesian learning-based methods [\[14\],](#page-9-13) [\[15\],](#page-9-14) [\[16\],](#page-9-15) [\[17\],](#page-9-16) [\[18\],](#page-9-17) [\[19\],](#page-9-18) [\[20\],](#page-10-0) [\[21\]](#page-10-1) and mixed ℓ2,<sup>0</sup> norm-based methods [\[22\].](#page-10-2)

<span id="page-0-9"></span><span id="page-0-8"></span><span id="page-0-7"></span><span id="page-0-6"></span><span id="page-0-5"></span>However, the above works did not consider the effect of imperfect antenna arrays. As a result, the performance of these algorithms is significantly affected in practical DOA estimation systems. In the literature, some work has started to investigate DOA estimation schemes under imperfect antenna arrays. For example, for an array with mutual coupling, gain or phase errors, and sensor location errors, a method for estimating DOA and model errors is proposed in [\[23\]. A](#page-10-3) fourth-order parallel factor decomposition model using imperfect waveforms is given in [\[24\]](#page-10-4) to estimate the DOA. Then, [\[25\]](#page-10-5) proposes a 2-D DOA estimation method for an imperfect L-shaped array using active calibration. However, each of the above works only considered a subset of the imperfect array effects because optimization over the complicated array model with all imperfect effects considered is challenging.

1557-9662 © 2024 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.

{1}------------------------------------------------

This motivates us to use the deep-learning (DL) technique for DOA estimation with all imperfect array effects taken into account because of its efficiency for training over difficult networks.

In the literature, several works have been done for DL-based DOA estimation [\[15\],](#page-9-14) [\[26\],](#page-10-6) [\[27\],](#page-10-7) [\[28\], a](#page-10-8)nd they have the advantages of low computational complexity and high accuracy. There are some types of DL-based methods:

- 1) The input data is the raw sampled data from the array;
- 2) The input data is the covariance matrix of the received signal;
- 3) The outputs are the directly estimated DOAs;
- 4) The output is the spatial spectrum and the DOAs are estimated from the spectrum.

Various DL-based methods have been proposed for DOA estimation in the literature. In [\[29\]](#page-10-9) and [\[30\], t](#page-10-10)he input is the covariance matrix, the output is the spectrum, and a sparse loss function is used to train the network. Papageorgiou et al. [\[31\]](#page-10-11) use the estimated covariance matrix as input and discretize the spatial domain into grids to estimate the DOA. A synthetic dataset is shown in [\[32\], a](#page-10-12)nd a CNN-based method is proposed for the estimation of DOA in the presence of additive noise, propagation attenuation, and delay. For coherent signals, an angle separation learning method is proposed in [\[30\],](#page-10-10) and the covariance matrix is formulated as input features of the DNN. In [\[30\], a](#page-10-10) deep convolution network (DCN) is given for DOA estimation with the covariance matrix as the undersampled linear measurements of the spatial spectrum, where the signal sparsity in the spatial domain is also exploited to improve estimation performance. A MUSIC-based DOA estimation method is proposed in [\[33\]](#page-10-13) using small antenna arrays, where DL is formulated to reconstruct the signals of a virtual large antenna array. Huang et al. [\[26\]](#page-10-6) gives an offline and online DNN method for the estimation of DOA in the massive multiple input multiple output (MIMO) system, where DOA is the network output and can be estimated directly from the received signal. For the estimation of DOA with a low signal-to-noise ratio (SNR), a convolutional neural network (CNN) is proposed in [\[31\], w](#page-10-11)here the covariance matrix is the input of the network and shows increased robustness in the presence of noise. Moreover, a multiple deep CNN is designed in [\[34\],](#page-10-14) where each CNN learns the MUSIC spectrum of the received signal, so a nonlinear relationship between the received sensor data and the angular spectrum is formulated in the network. For the imperfect array, [\[35\]](#page-10-15) introduces a DNN framework to estimate the DOA using a multitask autoencoder and a series of parallel multilayer classifiers.

<span id="page-1-6"></span>We find that the DL-based DOA estimation methods mainly use CNN as a typical network structure [\[36\], a](#page-10-16)nd the input is the statistic results such as the covariance matrix. Since the information in the statistical data limits the estimation performance, the performance cannot be better using the raw sampled data. Furthermore, the network output is the estimated DOAs, and the spatial spectrum cannot be obtained. Therefore, the network structure should be adjusted with different target <span id="page-1-0"></span>numbers and is not suitable for practical applications. There are some limitations to existing DL-based methods.

- 1) Since the classic DOA estimation algorithms, such as MUSIC, are just based on the covariance matrices of the received signals, most existing ML-based schemes use these covariance matrices as the input data to train the network. However, the covariance matrices are not sufficient for the optimal estimator design, in general. As a result, the input data used in these works do not preserve all useful information.
- 2) Furthermore, the output of existing ML-based DOA estimation schemes is usually the spatial spectrum of the targets. In this case, the training network depends on the number of targets, that is, different networks should be trained given a different number of targets. This is of high complexity in practice.
- <span id="page-1-3"></span><span id="page-1-2"></span><span id="page-1-1"></span>3) Furthermore, when the spatial spectrum is used, we must discretize the DOAs into grids, and the possible DOA must be on the discretized grids exactly. More girds as the output must be used for high accuracy, and the network will become more complex and difficult to train.

<span id="page-1-4"></span>In this article, we propose a DNN network based on CNN, that is, a super-resolution DOA network (SDOA-Net), to overcome the above-mentioned difficulties in the DOA estimation. The proposed SDOA-Net is used for the performance evaluation of imperfect arrays under realistic conditions. Compared with existing methods, the proposed SDOA-Net can achieve better estimation performance with lower complexity. The contributions of this article are given as follows.

- <span id="page-1-5"></span>1) *A System Model With Imperfect Array Effects for the DOA Estimation Is Formulated:* The imperfect effect includes the position perturbation, the inconsistent gains, the inconsistent phases, the mutual coupling effect, and the nonlinear effect. As a result, our results are directly applicable to a practical system.
- 2) *A DL Architecture Is Proposed Based on the Imperfect Array:* Unlike existing methods, the input of SDOA-Net is the raw sampled signals and the output is a vector, which can be easily used to estimate the spatial spectrum. Convolution layers are then used to get the signals' features and avoid the complexity of highdimension signals. The SDOA-Net output is a vector for the spectrum estimation and can avoid the problem of discretizing the spatial domain. Compared to the existing CNN-based method, the proposed SDOA-Net can be easily trained and perform better estimation.
- <span id="page-1-8"></span><span id="page-1-7"></span>3) *A Spatial Spectrum-Based Loss Function to Train the SDOA-Net Is Proposed:* where Gaussian functions are used to approximate the spatial spectrum. Inspired by the atomic norm minimization (ANM)-based DOA estimation method, the output of SDOA-Net is used to formulate the spatial spectrum. Different from existing networks for the DOA estimation, we use a special spectrum-based loss function to measure the error between the reference spectrum and the estimated one and to train the network.

{2}------------------------------------------------

The remainder of this article is organized as follows. The system mode of practical DOA estimation is formulated in Section II. The review of the super-resolution DOA estimation method is given in Section III. Then, the proposed SDOA-Net for DOA estimation is shown in Section IV. The simulation results are carried out in Section V, and finally Section VI concludes the article.

*Notations:* Matrices and column vectors are denoted by upper- and lower-case boldface letters, respectively. The matrix transpose and the Hermitian transpose are represented by  $(\cdot)^T$  and  $(\cdot)^H$ , respectively. The real and imaginary parts of a complex value are denoted by  $\mathcal{R}\cdot$  and  $\mathcal{I}\cdot$ , respectively. The trace of a matrix is denoted by  $\text{Tr}\cdot$ . The  $\ell_2$  norm is represented by  $|\cdot|_2$ .

#### <span id="page-2-0"></span>II. SYSTEM MODEL FOR PRACTICAL DOA ESTIMATION

In this article, we consider the DOA estimation problem in a practical system and propose a DL-based estimation framework. As shown in Fig. 1, we consider K far-field signals, and the kth  $(k=0,1,\ldots,K-1)$  signal is expressed as  $s_k(t) \in \mathbb{C}$  with the DOA being  $\theta_k \in (-(\pi/2), (\pi/2)]$ . A linear array system with N antennas is used to receive the signals and estimate the DOAs, where the wavelength is denoted as  $\lambda$ . Taking into account the additive noise  $w_n(t) \in \mathbb{C}$ , the signal received at the nth  $(n=0,1,\ldots,N-1)$  antenna can be expressed as

<span id="page-2-3"></span>
$$r_n(t) = g\left(x_n(t) + \sum_{n' \neq n} B_{n,n'} x_{n'}(t)\right) + w_n(t).$$
 (1)

Then, we have

$$x_n(t) = \sum_{k=0}^{K-1} s_k(t) A_n e^{j\phi_n} e^{j2\pi \frac{\mathrm{dn}}{\lambda} \sin \theta_k}$$
 (2)

where taking the zeroth antenna as the reference one, that is,  $d_0 = 0$ , the position of the *n*th antenna is  $d_n$ , and for a uniform linear array (ULA), the position of the antenna is  $d_n = n\lambda/2$ . In the received signal (1), the following imperfect problems are considered.

- 1) The Mutual Coupling Effect: The antennas cannot be ideally isolated and introduce the mutual coupling effect among the received signals. The mutual coupling coefficient between the nth and n'th  $(n \neq n')$  antenna is  $B_{n,n'} \in \mathbb{C}$  with  $|B_{n,n'}| < 1$  in (1).
- 2) The Position Perturbations: The antenna positions cannot be exactly at the desired positions and will cause phase errors of the received signals among antennas in the steering vector.
- 3) The Inconsistent Gains: The radio frequency (RF) channels usually cannot have exactly the same amplifiers and will cause amplitude differences among the received signals. The channel gain of the nth antenna is denoted as  $A_n > 0$ .
- 4) The Inconsistent Phases: The difference among the RF channels will also cause the delay and phase errors of the received signals, and the channel phase of the nth antenna is denoted as  $\phi_n$ .

<span id="page-2-2"></span>![](_page_2_Picture_14.jpeg)

Fig. 1. System model for the DOA estimation in a practical array.

5) The Nonlinear Effect: The nonlinear effect among RF channels and analog-to-digital converter (ADC) will introduce the nonlinear effect and degrade the DOA estimation performance. We use a nonlinear function  $g(\cdot)$  to represent the nonlinear operation in the receiving channels.

Hence, collect the received signals into a vector

$$\mathbf{r} \triangleq \left[r_0(t), r_1(t), \dots, r_{N-1}(t)\right]^{\mathrm{T}}.$$
 (3)

The DOA estimation problem can be formulated as a parameter estimation problem with the received signal r. Most existing works consider the methods in the scenario with the perfect array, where we have the linear function  $g(\cdot)$ , the mutual coupling coefficient  $B_{n,n'}$  is 0, the channel gains are the same  $(A_n = 1 \text{ and } \phi_0 = 0)$ , and the position  $d_n$  of the antenna is known.

However, when an imperfect array is considered, the imperfect elements include the mutual coupling effect, the nonlinear effect, the inconsistent phases, the inconsistent gains, and the position perturbations. In the practical systems, most existing super-resolution methods cannot outperform the traditional methods, where the super-resolution methods must have perfect systems and high SNR. In this article, we will focus on a robust super-resolution method for DOA estimation with imperfect system effects.

# III. REVIEW OF SUPER-RESOLUTION DOA ESTIMATION METHODS

#### <span id="page-2-1"></span>A. Atomic Norm-Based Estimation Methods

In recent years, atomic norm-based methods have been proposed for line-spectral estimation and achieved better performance by exploiting the sparsity of the spectrum in the frequency domain. Additionally, the DOA estimation problem 

{3}------------------------------------------------

can be easily described as a line-spectral estimation problem, so atomic norm-based methods have been proposed for the DOA estimation.

Usually, in the atomic norm-based methods. the ideal ULA is assumed, and the received signal based on (1) in the nth array can be expressed as

$$r_n = \sum_{k=0}^{K-1} s_k e^{j2\pi \frac{\text{nd}}{\lambda} \sin \theta_k} + w_n(t)$$
 (4)

where the distance between adjacent antennas is  $d = (\lambda/2)$ . Then, with the definition of a steering vector

$$\boldsymbol{a}(\theta) \triangleq \left[1, e^{j\frac{2\pi d}{\lambda}\sin\theta}, \dots, 1, e^{j\frac{2\pi(N-1)d}{\lambda}\sin\theta}\right]^{\mathrm{T}}$$
 (5)

collect all the received signals into a vector, and we have

$$\mathbf{r} \triangleq \begin{bmatrix} r_0, r_1, \dots, r_{N-1} \end{bmatrix}^{\mathrm{T}}$$
  
=  $\mathbf{A}\mathbf{s} + \mathbf{w}$  (6)

where we define the steering matrix as

$$\mathbf{A} \triangleq \left[ \mathbf{a}(\theta_0), \mathbf{a}(\theta_1), \dots, \mathbf{a}(\theta_{K-1}) \right] \tag{7}$$

the signal vector is defined as

$$\mathbf{s} \triangleq \left[ s_0, s_1, \dots, s_{K-1} \right]^{\mathrm{T}} \tag{8}$$

and the noise vector is

$$\boldsymbol{w} \triangleq \left[w_0, w_1, \dots, w_{N-1}\right]^{\mathrm{T}}.\tag{9}$$

In the ANM-based DOA estimation method, an atomic norm is defined as

$$\|\boldsymbol{x}\|_{\mathcal{A}} \triangleq \inf \left\{ \sum_{n} \alpha_{n'} : \boldsymbol{x} = \sum_{n'} \alpha_{n'} e^{j\phi_{n'}} \boldsymbol{a}(\theta_{n'}) \right.$$
$$\phi_{n'} \in [0, 2\pi), \alpha_{n'} \geq 0 \right\} \quad (10)$$

which describes a sparse representation of x with the sparse coefficients being  $\alpha_{n'}$  (n' = 0, 1, ..., N' - 1). Then, with the received signal r, we denoise the signal with a sparse reconstruction signal x, which can be expressed as an ANM expression

$$\min_{\mathbf{r}} \frac{1}{2} \|\mathbf{r} - \mathbf{x}\|_{2}^{2} + \beta \|\mathbf{x}\|_{\mathcal{A}}$$
 (11)

where the parameter  $\beta$  is used to control the tradeoff between the sparsity and the reconstruction accuracy. This ANM problem can be solved by introducing a semi-definite programming (SDP) method, which is

<span id="page-3-1"></span>
$$\min_{\boldsymbol{B},\boldsymbol{h}} \|\boldsymbol{r} - \boldsymbol{h}\|_{2}^{2}$$
s.t  $\begin{bmatrix} \boldsymbol{B} & \boldsymbol{h} \\ \boldsymbol{h}^{H} & 1 \end{bmatrix} \succeq 0$ 
 $\boldsymbol{B}$  is Hermitian matrix
$$\operatorname{Tr}\{\boldsymbol{B}\} = \beta^{2}$$

$$\sum_{n} \boldsymbol{B}_{n,n+n'} = 0, \text{ for } n' \neq 0$$
and  $n' = 1 - N, \dots, N - 1.$  (12)

By solving the SDP problem (12), the sparse reconstruction signal h can be obtained, and the DOA of the received signal can be estimated by finding the peak values of the following polynomial:

<span id="page-3-2"></span>
$$f(\theta) = |\mathbf{a}^{\mathrm{H}}(\theta)\mathbf{h}|^{2}. \tag{13}$$

<span id="page-3-3"></span>The ANM-based DOA estimation method is for the ideal array with perfect assumptions, but for the practical array, the ANM-based method must be extended. In [37], [38], [39], and [40], the atomic norm-based methods are extended for the practical array. We can find that the much more complex optimization problems are formulated, and a vector like h denoted as h' can be obtained. Then, the DOAs are estimated by the peak values of the following polynomial:

$$f'(\theta) = |\mathbf{a}^{\mathrm{H}}(\theta)\mathbf{h}'|^{2}. \tag{14}$$

#### B. MUSIC-Based Estimated Methods

In the super-resolution estimation method, the MUSIC-based methods can perform better by using noise and signal subspaces. For single-snapshot spectral estimation, Liao and Fannjiang [41] propose a MUSIC-based method. A Hankel matrix is obtained from the received signal r as

<span id="page-3-4"></span>
$$\mathbf{R} = \text{Hankel}(\mathbf{r}) \begin{bmatrix} r_0 & r_1 & \cdots & r_{N-L} \\ r_1 & r_2 & \cdots & r_{N-L+1} \\ \vdots & \vdots & \ddots & \vdots \\ r_{L-1} & r_L & \cdots & r_{N-1} \end{bmatrix}$$
(15)

where the received signal r is reshaped as a matrix  $R \in \mathbb{C}^{L \times N - L + 1}$ . Then, a singular value decomposition (SVD) is used as

$$[\boldsymbol{U}_1, \boldsymbol{U}_2] \boldsymbol{\Lambda} [\boldsymbol{V}_1, \boldsymbol{V}_2] = \text{SVD} \{\boldsymbol{R}\}$$
 (16)

where  $U_2$  is corresponding to the small singular values and  $\Lambda$  is a diagonal matrix with the entries from the singular values. Finally, the spatial spectrum can be estimated as

$$g(\theta) = \frac{1}{\|\mathbf{a}^{H}(\theta)\mathbf{U}_{2}\|_{2}^{2}}.$$
 (17)

#### IV. PROPOSED DOA ESTIMATION METHOD

<span id="page-3-0"></span>From the above sections about the existing DOA estimation methods, we can find that the DOAs are estimated by searching the peak values of the spatial spectrum. In this section, we will propose a DL-based super-resolution method for DOA estimation, it is named SDOA-Net, which contains more information and can be trained faster than the existing covariance matrix-based methods.

#### A. Architecture of SDOA-Net

The SDOA-Net architecture is shown in Fig. 2. First, the received signal in (1) is rewritten as a vector with real and imaginary parts

$$\mathbf{v}(t) \triangleq [\mathcal{R}^{\mathrm{T}}\{\mathbf{r}(t)\}, \mathcal{I}^{\mathrm{T}}\{\mathbf{r}(t)\}]^{\mathrm{T}} \in \mathbb{R}^{2N \times 1}$$
 (18)

{4}------------------------------------------------

<span id="page-4-0"></span>![](_page_4_Figure_2.jpeg)

Fig. 2. Network architecture of the proposed SDOA-Net.

where we have the received signal vector

$$\mathbf{r}(t) = [r_0(t), r_1(t), \dots, r_{N-1}(t)]^{\mathrm{T}} \in \mathbb{C}^{N \times 1}.$$
 (19)

With the batch size being  $M_R$ , the input signal is

$$Y \triangleq [y(0), y(1), \dots, y(M_B - 1)]^{\mathrm{T}}$$
 (20)

and the size is  $M_R \times 2N$ .

Then, since the SDOA-Net is based on the convolution network, we use a full connection (FC) as the input layer with the output dimension being  $M_FM_I$ , where  $M_F$  denotes the number of filters in the convolution layers and  $M_I$  denotes the extension of the inner dimension. After the input layer, the dimension of the signal is  $M_B \times M_FM_I$ , and we reshape the signal as a tensor  $f_1(Y)$  with the dimension  $M_B \times M_F \times M_I$ , where  $f_1(\cdot)$  is an input layer function.

The tensor is passed to the convolution layers and the number of convolution layers is  $M_C$ . In each convolution layer, a 1-D convolution operation is realized with the kernel size being  $M_F \times M_K$  and the padding operation is used to keep the size of the convolution output the same as that of the input. The output of the convolution operation is  $M_B \times M_F \times M_I$ . Then, the batch normalization is applied to the convolution output, and the normalization output is denoted as  $f_3(f_2(f_1(Y)))$ . The function  $f_2(\cdot)$  denotes the convolution operation and  $f_3(\cdot)$  is the batch normalization operation

$$f_3(x) = \frac{x - \mathcal{E}\{x\}}{\sqrt{\text{Var}\{x\} + \epsilon}}$$
 (21)

where  $\mathcal{E}\{x\}$  and  $\mathrm{Var}\{x\}$  are the mean and variance of x, respectively.  $\epsilon$  is a value added to the denominator for numerical stability and can be set as  $\epsilon=10^{-5}$ . In each convolution layer, a ReLU function  $f_4(\cdot)$  is applied to the output of the batch normalization and is defined as

$$f_4(x) \triangleq \max(0, x). \tag{22}$$

After the convolution layers, an FC layer is used as an output layer with the input and output sizes being  $M_B \times M_I M_F$  and  $M_B \times 2N$ , respectively. The operation in the output layer is denoted as  $f_5(\cdot)$ .

Finally, as shown in Fig. 3, we can obtain the output of the SDOA-Net as

$$G = f_5(f_4(f_3(f_2(f_4(\dots f_4(\dots f_2(f_1(Y))\dots))))))$$
 (23)

<span id="page-4-1"></span>![](_page_4_Picture_17.jpeg)

Fig. 3. Flowchart of the functional operations.

where we have

$$G \triangleq [g(0), g(1), \dots, g(M_B - 1)] \in \mathbb{R}^{2N \times M_B}.$$
 (24)

As shown in Fig. 4, the corresponding complex vector can be obtained from the network output g(m)  $(m = 0, 1, ..., M_B - 1)$  as

$$z(m) \triangleq \mathbf{g}_{0:N-1}(m) + j\mathbf{g}_{N:2N-1}(m)$$
 (25)

where  $\mathbf{g}_{0:N-1}(m)$  denotes a subvector of  $\mathbf{g}(m)$  with the index from 0 to N-1, and  $\mathbf{g}_{N:2N-1}(m)$  denotes that from N to 2N-1. With the output  $\mathbf{z}$  of SDOA-Net, the spatial spectrum can be estimated by

<span id="page-4-2"></span>
$$f_{\rm sp}(\zeta) = |\boldsymbol{a}^{\rm H}(\zeta)\boldsymbol{z}|^2 \tag{26}$$

where  $\zeta$  is chosen based on the detection area, such as from  $-\pi/2$  to  $\pi/2$ .

The SDOA-Net proposed in this study introduces a novel approach compared to existing methods. Unlike previous approaches, our network takes raw sampled data as input and utilizes convolution layers to extract features from these raw

{5}------------------------------------------------

<span id="page-5-0"></span>![](_page_5_Figure_2.jpeg)

Fig. 4. Flowchart to obtain the spatial spectrum from the network output.

data. By using the raw data, which contains all the information of the received signals, we obtain a vector as the network's output. This output vector is distinct from the DOA results or the spatial spectrum used by existing methods. In particular, the size of the output vector matches the number of antennas in the array, resulting in a lower dimension compared to networks that output the spectrum. Consequently, training time can be significantly reduced. Furthermore, DOAs can be obtained by finding the peak values of  $f_{\rm sp}(\zeta)$  in (26), which can avoid the problem of adopting the determined number of received signals in networks using DOA values as output.

#### B. Training Approach

To train the SDOA-Net, the spatial spectrum  $f_{sp}(\zeta)$  is obtained from (26) and the refereed spectrum is given as follows:

$$f_{\text{ref}}(\zeta) = \sum_{k=0}^{K-1} A_k e^{-\frac{(\zeta - \theta_k)^2}{\sigma_G^2}}$$
 (27)

where we use Gaussian functions to approximate the spatial spectrum.  $A_k$  denotes the spectrum value, and  $\sigma_G$  is the standard deviation of the Gaussian function. In this article, we set the value of  $\sigma_G$  as

$$\sigma_G = \bar{\sigma}_G/N. \tag{28}$$

An example of the referenced spatial spectrum approximated by the Gaussian functions is shown in Fig. 5, where we use 16 antennas,  $\bar{\sigma}_G = 100$ , and the ground-truth DOAs are  $-30^\circ$ ,  $10^\circ$ , and  $20^\circ$ . The width of the 3 dB spectrum is about  $10.4^\circ$ . With the refereed spectrum, the loss function is defined as

<span id="page-5-2"></span>
$$f_{\text{loss}}(\zeta) = \frac{1}{\Omega} \| f_{\text{ref}}(\zeta) - f_{\text{sp}}(\zeta) \|_2^2$$
 (29)

where  $f_{\rm ref}(\zeta) \in \mathbb{R}^{\Omega \times 1}$  and  $f_{\rm sp}(\zeta) \in \mathbb{R}^{\Omega \times 1}$  are vectors with the  $\omega$ -th  $(\omega = 0, 1, \ldots, \Omega - 1)$  entry being  $f_{\rm ref}(\zeta_{\omega})$  and  $f_{\rm sp}(\zeta_{\omega})$ , respectively. We define

$$\boldsymbol{\zeta} \triangleq \left[\zeta_0, \dots, \zeta_{\Omega-1}\right]^{\mathrm{T}} \tag{30}$$

<span id="page-5-1"></span>![](_page_5_Figure_14.jpeg)

Fig. 5. Refereed spatial spectrum approximated by the Gaussian functions.

where  $\Omega$  is the number of the discretized spatial angles. The SDOA-Net is trained to minimize the loss function  $f_{loss}(\zeta)$  in (29) by updating the network coefficients.

For the practical system, the mutual coupling effect, the nonlinear effect, the inconsistent phases, the inconsistent gains, and the position perturbations are considered in this article. The training procedure is shown in Fig. 6, and the following steps can be used to train the SDOA-Net.

- Perfect Array Step: The received signals using a perfect array without the imperfect effect are used during the training procedure.
- 2) Position Perturbation Step: The received signals with position perturbation are used. The position perturbation is generated by a Gaussian distribution with the mean being 0 and the standard deviation  $\sigma_{per}$  selected by a uniform distribution  $\sigma_{per} \in [0, \sigma_{max\_per}]$ . The parameter  $\sigma_{max\_per}$  can be specified in the simulation.
- 3) *Inconsistent Gains Step:* The inconsistent gains are considered in this step. Similarly, the inconsistent gains are generated by a zero-mean Gaussian distribution with the standard deviation  $\sigma_{gain}$  being  $\sigma_{gain} \in [0, \sigma_{max\_gain}]$ , where  $\sigma_{max\_gain}$  is specified in the simulation.
- 4) *Inconsistent Phases Step:* The inconsistent phases are also generated by a zero-mean Gaussian distribution with the standard deviation  $\sigma_{\text{phase}}$  being  $\sigma_{\text{phase}} \in [0, \sigma_{\text{max\_phase}}]$ , where  $\sigma_{\text{max\_phase}}$  is specified in the simulation.
- 5) *Mutual Coupling Effect Step:* The mutual coupling effect is described by a matrix **B** with complex entries, and the diagonal entries are all ones. The entry at the *n*th row and the *n*'th column is denoted as

$$B_{n,n'} = |B_{n,n'}|e^{j\psi_{n,n'}}$$
(31)

and  $|B_{n,n'}|$  is determined by a uniform distribution  $|B_{n,n'}| \in [0, \sigma_{\mathrm{mc}}^{|n-n'|}]$  with  $n \neq n'$ . The phase  $\psi_{n,n'}$ 

{6}------------------------------------------------

<span id="page-6-1"></span>![](_page_6_Figure_2.jpeg)

Fig. 6. Training procedure for the SDOA-Net.

follows a uniform distribution ψ*<sup>n</sup>*,*<sup>n</sup>* ′ ∈ [0, 2π ). The parameter σmc is specified in the simulation.

6) *Nonlinear Effect Step:* The nonlinear effect is described by a nonlinear function

$$f_{\text{nonlinear}}(x) = \tanh(x\sigma_{\text{nonlinear}})$$
 (32)

where σnonlinear is specified in the simulation to control the nonlinear effect. The tanh(·) function is used as a nonlinear function. Usually, we can also use other types of activation functions, such as ReLU, leaky ReLU, sigmoid, and so on, and the choice of activation function will not have a big impact on the performance of the DOA estimation.

7) *All the Imperfect Effect Step:* We consider all the imperfect effects to train the network.

The network is trained to the next step after all the data is used in the current step. For example, when we use all the data in the inconsistent phases step, we go to the next step of the mutual coupling effect. After training SDOA-Net in sequence according to the above steps, we start over from the first step to train the network again until the maximum number of training procedures.

# V. SIMULATION RESULTS

<span id="page-6-0"></span>In this section, the DOA estimation performance of the proposed SDOA-Net using a practical array is evaluated through simulation. The simulations are conducted on a computer with MATLAB R2020b, equipped with an Intel Core i5 at 2.9 GHz processor and 8 GB LPDDR3 at 2133 MHz. The SDOA-Net source code, including the training codes and a pretrained network, is available at https://github.com/chenpengseu/SDOA-Net.git. SDOA-Net is

TABLE I SIMULATION PARAMETERS

<span id="page-6-2"></span>

| Parameter                                           | Value                        |
|-----------------------------------------------------|------------------------------|
| The standard deviation in the Gaussian function     | $\bar{\sigma}_{\rm G} = 100$ |
| The batch size                                      | 64                           |
| The number of convolution layers                    | 6                            |
| The number of filters in the convolution layer      | $^2$                         |
| The kernel size in the convolution layer            | 3                            |
| The learning rate                                   | $5 \times 10^{-4}$           |
| The number of antennas $N$                          | 16                           |
| The number of targets $K$                           | 3                            |
| The distance between adjacent antennas              | $0.5\lambda$                 |
| The maximum standard deviation of                   | 0.15                         |
| position perturbation $\sigma_{\text{max\_per}}$    |                              |
| The maximum standard deviation of                   | 0.5                          |
| inconsistent gain $\sigma_{	ext{max\_gain}}$        |                              |
| The maximum standard deviation of                   | 0.2                          |
| inconsistent phase $\sigma_{\text{max\_phase}}$     |                              |
| The maximum mutual coupling effect $\sigma_{ m mc}$ | 0.06                         |
| The nonlinear effect $\sigma_{\text{nonlinear}}$    | 1.0                          |

based on PyTorch 1.4 and Python 3.7. The simulation parameters are given in Table [I.](#page-6-2) We use *N* = 16 antennas to receive the signals and the SDOA-Net to estimate the DOA, where the number of signals is *K* = 3. Moreover, the hyperparameters for the imperfect array are also given in Table [I.](#page-6-2) The estimation performance is measured by the root mean square error (RMSE)

$$RMSE = \sqrt{\frac{1}{N_{sim}K} \|\hat{\boldsymbol{\theta}} - \boldsymbol{\theta}\|_{2}^{2}}$$
 (33)

where *<sup>N</sup>*sim is the number of simulations, <sup>ˆ</sup><sup>θ</sup> is the estimated DOA vector, and θ is the ground-truth DOA vector.

First, the proposed SDOA-Net contains convolution layers and each convolution layer has convolution, batch normalization, and ReLU active function operations. In SDOA-Net, some important hyperparameters must be considered for a better DOA estimation. The first hyperparameter is the number of 1D convolution layers. In Fig. [7,](#page-7-0) we show the performance of the DOA estimation with different numbers of convolution layers. As shown in this figure, when the number of convolutions is 6, a better estimation performance is achieved, so we use 6 convolution layers in the following simulations.

Then, we compare the DOA estimation performance among the networks using different numbers *M<sup>F</sup>* of filters that are used in the convolution layers. As shown in Fig. [8,](#page-7-1) for the consideration of both the estimation performance and the network complexity, better performance is achieved with *M<sup>F</sup>* = 2, so we will use two filters in the following simulations. Note that selecting optimal values for individual parameters does not necessarily ensure that the network configuration will attain the global optimum. Nonetheless, by comparing the network's performance across various parameter settings, we can assess the influence of distinct parameters on the network's overall

{7}------------------------------------------------

<span id="page-7-0"></span>![](_page_7_Figure_2.jpeg)

Fig. 7. DOA estimation performance with different numbers of layers.

<span id="page-7-1"></span>![](_page_7_Figure_4.jpeg)

Fig. 8. DOA estimation performance with different numbers of filters.

performance. This analysis facilitates informed the selection of network parameters.

In the procedure of training the SDOA-Net, the referred spatial spectrum is used to measure the loss function, where we use the Gaussian functions to approximate the spatial spectrum. Hence, the standard deviation σ¯ *<sup>G</sup>* in the Gaussian function is important to approximating the spatial spectrum. We show the performance of DOA estimation with different standard deviations σ¯ *<sup>G</sup>* in Fig. [9.](#page-7-2) When the standard deviation σ¯ *<sup>G</sup>* is 100, better performance of DOA estimation is achieved, so we will use σ¯ *<sup>G</sup>* = 100 in the following simulation.

Next, based on the above SDOA-Net parameters, the estimated spatial spectrum is shown in Fig. [10](#page-7-3) for the DOA estimation and is also compared with the following existing methods.

1) *MUSIC Method [\[41\]:](#page-10-21)* The conventional MUSIC method estimates the covariance matrix based on multiple snapshots and employs eigenvalue decomposition to estimate DOA. To make a fair comparison, we adopt

<span id="page-7-2"></span>![](_page_7_Figure_10.jpeg)

Fig. 9. DOA estimation performance with different standard deviations σ¯ *<sup>G</sup>* .

<span id="page-7-3"></span>![](_page_7_Figure_12.jpeg)

Fig. 10. Spatial spectrum compared with the existing methods.

- <span id="page-7-4"></span>the snapshot-based MUSIC algorithm proposed in [\[41\]](#page-10-21) that utilizes a Hankel data matrix and Vandermonde decomposition in the MUSIC method.
- 2) *ANM Method [\[39\],](#page-10-19) [\[42\],](#page-10-22) [\[43\]:](#page-10-23)* ANM-based methods have been introduced for DOA estimation, which can take advantage of the sparsity of the targets in the spatial domain. In contrast to current CS-based methods, which involve discretizing the spatial domain into grids and using a dictionary matrix for sparse reconstruction, such as those proposed in [\[44\],](#page-10-24) [\[45\], a](#page-10-25)nd [\[46\], A](#page-10-26)NM methods estimate DOA in the continuous domain. This approach can overcome the *off-grid* problem caused by discrete methods.
- <span id="page-7-6"></span><span id="page-7-5"></span>3) *FFT Method:* The FFT method is widely used in practical systems with low computational complexity. However, the resolution of the FFT method is unsatisfactory but robust to the imperfect array.

{8}------------------------------------------------

<span id="page-8-0"></span>![](_page_8_Figure_2.jpeg)

![](_page_8_Figure_3.jpeg)

4) *OMP Method* [47], [48], [49]: The orthogonal matching pursuit (OMP) method is a CS-based method using the discretized spatial angles and has relatively low computational complexity. Hence, it has been widely used in sparse reconstruction problems.

As shown in Fig. 10, the spatial spectrum estimated by the proposed SDOA-Net performs better than the MUSIC, ANM, FFT, and OMP methods. Additionally, the proposed method is based on the convolution network and has lower computational complexity than the ANM and MUSIC methods. The computational complexity of the proposed network is  $\mathcal{O}(N^2)$ , and the computational complexities of ANM and MUSIC are  $\mathcal{O}((N+1)^{6.5})$  and  $\mathcal{O}(N^3)$ , respectively. Therefore, the proposed SDOA-Net is efficient in the DOA estimation problem.

Next, the performance of the DOA estimation under different SNRs is shown in Fig. 11, where the SNR ranges from 0 to 30 dB. This figure shows that the proposed method achieves a better estimation performance in the scenario with an imperfect array than the method using the ANM, FFT, MUSIC, and OMP methods. For the SNR being 10 dB, the RMSE of the proposed SDOA-Net is about 0.70° and that of the ANM method is about 1.15°, so the RMSE improvement is about 39.13%. Furthermore, when the SNR is 7.5 dB, the RMSE of the proposed SDOA-Net method is the same as that of the ANM method with the SNR being 15 dB, so the improvement in the SNR is about 7.5 dB.

We use an imperfect factor to measure the imperfect effect, defined as  $\xi$ . With the imperfect factor  $\xi$ , the imperfect parameters for position perturbation, inconsistent gain, inconsistent phase, mutual coupling effect and nonlinear effect will be  $\xi\sigma_{\text{max\_per}}$ ,  $\xi\sigma_{\text{max\_gain}}$ ,  $\xi\sigma_{\text{max\_phase}}$ ,  $\xi\sigma_{\text{mc}}$ , and  $\xi\sigma_{\text{nonlinear}}$ , respectively. For example, as presented in Table I, the maximum standard deviation of position perturbation is denoted as  $\sigma_{\text{max\_per}} = 0.15$ . Given an imperfection factor of  $\xi = 0.5$ , the standard deviation of position perturbation for the simulations is adjusted to  $\xi\sigma_{\text{max\_per}} = 0.5 \times 0.15 = 0.075$ . To evaluate

<span id="page-8-1"></span>![](_page_8_Figure_8.jpeg)

Fig. 12. DOA estimation performance with different imperfect factors.

<span id="page-8-2"></span>the DOA estimation performance across various scenarios, we vary the imperfection factor from 0.1 to 1.0.

Fig. 12 illustrates the performance of DOA estimation when considering various imperfect factors. The SDOA-Net method, proposed in this study, outperforms the compared methods in terms of accuracy of estimation. Moreover, the proposed method demonstrates superior performance in scenarios with higher imperfect factors, indicating its robustness against the negative impact of imperfections.

<span id="page-8-3"></span>In addition, [50] also introduces a DL-based approach to estimate the DOA, known as the deep frequency network. This method utilizes the network output as the spectrum. Fig. 13 illustrates the spatial spectrum of both the proposed SDOA-Net and the deep frequency network. It can be observed that the estimated spectrum from the deep frequency network is less smooth compared to that of the proposed SDOA-Net since the output of the deep frequency network is the spatial spectrum. Consequently, SDOA-Net demonstrates superior DOA estimation performance compared to the deep frequency network.

Fig. 14 illustrates the performance of DOA estimation at varying SNRs, ranging from 0 to 30 dB. Both the SDOA-Net and the deep frequency network employ the same training dataset. From the DOA estimation performance, it can be found that the deep frequency network does not achieve a better DOA estimation performance, mainly because of the following two reasons.

- The spatial spectrum obtained by the deep frequency network is not smooth enough, which makes it easy to incorrectly select the peak value of the spatial spectrum and fail to obtain the DOA information.
- 2) The deep frequency network has high accuracy for the DOA estimation of the perfect array [50], but its efficacy considerably diminishes for the imperfect array due to the lack of specific optimization for robustness.

Consequently, when compared to traditional model-based approaches such as FFT and OMP methods, the deep

{9}------------------------------------------------

<span id="page-9-20"></span>![](_page_9_Figure_2.jpeg)

Fig. 13. Spatial spectrum compared with the existing DL-based method.

<span id="page-9-21"></span>![](_page_9_Figure_4.jpeg)

Fig. 14. DOA estimation performance compared with the existing DL-based method.

frequency network exhibits inferior performance. The performance of the proposed SDOA-Net surpasses that of existing methods such as the FFT method, the OMP method, and the deep frequency network. The proposed SDOA-Net is tailored for imperfect arrays and generates a smoother output spatial spectrum, which simplifies the process of accurately identifying the spectral peaks during the peak-search stage. Consequently, this enhancement enables the proposed SDOA-Net to achieve improved DOA estimation performance for the imperfect array.

# VI. CONCLUSION

<span id="page-9-19"></span>The problem of estimating the DOA has been studied in the context of an imperfect array. A system model has been developed to account for various factors such as antenna position perturbations, inconsistent gains and phases, mutual coupling effect, and nonlinear effect. To address this problem, a novel method, called SDOA-Net, has been introduced. Unlike existing approaches, SDOA-Net takes raw sampled signals as input and produces a vector that can be used to estimate the spatial spectrum. By utilizing convolution layers, SDOA-Net achieves faster convergence in training compared to other DL-based methods. The simulation results demonstrate the advantages of SDOA-Net in DOA estimation using a practical array. For an SNR of 10 dB, the RMSE in DOA estimation achieved through the proposed method exhibits a 39.13% improvement over the performance of the ANM method. In the future, further research will focus on the theoretical analysis of SDOA-Net's performance in DOA estimation.

#### REFERENCES

- <span id="page-9-0"></span>[\[1\]](#page-0-0) Q. Tian and R. Cai, "A low-complexity DOA estimation algorithm for distributed source localization," *IEEE Trans. Instrum. Meas.*, vol. 72, pp. 1–4, 2023.
- <span id="page-9-1"></span>[\[2\]](#page-0-0) J. A. Zhang et al., "An overview of signal processing techniques for joint communication and radar sensing," *IEEE J. Sel. Topics Signal Process.*, vol. 15, no. 6, pp. 1295–1315, Nov. 2021.
- <span id="page-9-2"></span>[\[3\]](#page-0-0) M. Pan et al., "Efficient joint DOA and TOA estimation for indoor positioning with 5G picocell base stations," *IEEE Trans. Instrum. Meas.*, vol. 71, pp. 1–19, 2022.
- <span id="page-9-3"></span>[\[4\]](#page-0-0) C. Xu, B. Clerckx, S. Chen, Y. Mao, and J. Zhang, "Rate-splitting multiple access for multi-antenna joint radar and communications," *IEEE J. Sel. Topics Signal Process.*, vol. 15, no. 6, pp. 1332–1347, Nov. 2021.
- <span id="page-9-4"></span>[\[5\]](#page-0-1) L. Zhu, S. Qiu, and Y. Han, "Combined constrained adaptive sum and difference beamforming in monopulse angle estimation," *IEEE Antennas Wireless Propag. Lett.*, vol. 17, no. 12, pp. 2314–2318, Dec. 2018.
- <span id="page-9-5"></span>[\[6\]](#page-0-2) J.-D. Lin, W.-H. Fang, Y.-Y. Wang, and J.-T. Chen, "FSF MUSIC for joint DOA and frequency estimation and its performance analysis," *IEEE Trans. Signal Process.*, vol. 54, no. 12, pp. 4529–4542, Dec. 2006.
- <span id="page-9-6"></span>[\[7\]](#page-0-2) F. Yan, M. Jin, and X. Qiao, "Low-complexity DOA estimation based on compressed MUSIC and its performance analysis," *IEEE Trans. Signal Process.*, vol. 61, no. 8, pp. 1915–1930, Apr. 2013.
- <span id="page-9-7"></span>[\[8\]](#page-0-2) X. Zhang, L. Xu, L. Xu, and D. Xu, "Direction of departure (DOD) and direction of arrival (DOA) estimation in MIMO radar with reduced-dimension MUSIC," *IEEE Commun. Lett.*, vol. 14, no. 12, pp. 1161–1163, Dec. 2010.
- <span id="page-9-8"></span>[\[9\]](#page-0-3) S. Kim, D. Oh, and J. Lee, "Joint DFT-ESPRIT estimation for TOA and DOA in vehicle FMCW radars," *IEEE Antennas Wireless Propag. Lett.*, vol. 14, pp. 1710–1713, 2015.
- <span id="page-9-9"></span>[\[10\]](#page-0-3) J. Lin, X. Ma, S. Yan, and C. Hao, "Time-frequency multi-invariance ESPRIT for DOA estimation," *IEEE Antennas Wireless Propag. Lett.*, vol. 15, pp. 770–773, 2016.
- <span id="page-9-10"></span>[\[11\]](#page-0-3) X. Zhang, X. Gao, and D. Xu, "Multi-invariance ESPRIT-based blind DOA estimation for MC-CDMA with an antenna array," *IEEE Trans. Veh. Technol.*, vol. 58, no. 8, pp. 4686–4690, Oct. 2009.
- <span id="page-9-11"></span>[\[12\]](#page-0-3) F.-M. Han and X.-D. Zhang, "An ESPRIT-like algorithm for coherent DOA estimation," *IEEE Antennas Wireless Propag. Lett.*, vol. 4, pp. 443–446, 2005.
- <span id="page-9-12"></span>[\[13\]](#page-0-4) F. Chen, D. Yang, and S. Mo, "A DOA estimation algorithm based on eigenvalues ranking problem," *IEEE Trans. Instrum. Meas.*, vol. 72, pp. 1–15, 2023.
- <span id="page-9-13"></span>[\[14\]](#page-0-5) Q. Guo, Z. Xin, T. Zhou, and S. Xu, "Off-grid space alternating sparse Bayesian learning," *IEEE Trans. Instrum. Meas.*, vol. 72, pp. 1–10, 2023.
- <span id="page-9-14"></span>[\[15\]](#page-0-5) L. Wan, Y. Sun, L. Sun, Z. Ning, and J. J. P. C. Rodrigues, "Deep learning based autonomous vehicle super resolution DOA estimation for safety driving," *IEEE Trans. Intell. Transp. Syst.*, vol. 22, no. 7, pp. 4301–4315, Jul. 2021.
- <span id="page-9-15"></span>[\[16\]](#page-0-5) P. Chen, Z. Cao, Z. Chen, and X. Wang, "Off-grid DOA estimation using sparse Bayesian learning in MIMO radar with unknown mutual coupling," *IEEE Trans. Signal Process.*, vol. 67, no. 1, pp. 208–220, Jan. 2019.
- <span id="page-9-16"></span>[\[17\]](#page-0-5) S. Jiang, N. Fu, Z. Wei, Z. Lian, L. Qiao, and X. Peng, "Compressed sampling for spectrum measurement and DOA estimation with array cooperative MWC," *IEEE Trans. Instrum. Meas.*, vol. 72, pp. 1–14, 2023.
- <span id="page-9-17"></span>[\[18\]](#page-0-5) J. Dai and H. C. So, "Real-valued sparse Bayesian learning for DOA estimation with arbitrary linear arrays," *IEEE Trans. Signal Process.*, vol. 69, pp. 4977–4990, 2021.
- <span id="page-9-18"></span>[\[19\]](#page-0-5) Y. Mao, Q. Guo, J. Ding, F. Liu, and Y. Yu, "Marginal likelihood maximization based fast array manifold matrix learning for direction of arrival estimation," *IEEE Trans. Signal Process.*, vol. 69, pp. 5512–5522, 2021.

{10}------------------------------------------------

- <span id="page-10-0"></span>[\[20\]](#page-0-5) J. Wan, C. Wang, P. Shen, H. Fu, and J. Zhu, "Robust and fast super-resolution SAR tomography of forests based on covariance vector sparse Bayesian learning," *IEEE Geosci. Remote Sens. Lett.*, vol. 19, pp. 1–5, 2022.
- <span id="page-10-1"></span>[\[21\]](#page-0-5) L. Wang, L. Zhao, S. Rahardja, and G. Bi, "Alternative to extended block sparse Bayesian learning and its relation to pattern-coupled sparse Bayesian learning," *IEEE Trans. Signal Process.*, vol. 66, no. 10, pp. 2759–2771, May 2018.
- <span id="page-10-2"></span>[\[22\]](#page-0-6) M. M. Hyder and K. Mahata, "Direction-of-arrival estimation using a mixed ℓ2,<sup>0</sup> norm approximation," *IEEE Trans. Signal Process.*, vol. 58, no. 9, pp. 4646–4655, Sep. 2010.
- <span id="page-10-3"></span>[\[23\]](#page-0-7) R. Lu, M. Zhang, X. Liu, X. Chen, and A. Zhang, "Direction-ofarrival estimation via coarray with model errors," *IEEE Access*, vol. 6, pp. 56514–56525, 2018.
- <span id="page-10-4"></span>[\[24\]](#page-0-8) N.-J. Ruan, F.-Q. Wen, L. Ai, and K. Xie, "A PARAFAC decomposition algorithm for DOA estimation in colocated MIMO radar with imperfect waveforms," *IEEE Access*, vol. 7, pp. 14680–14688, 2019.
- <span id="page-10-5"></span>[\[25\]](#page-0-9) S. Liu, Z. Zhang, and Y. Guo, "2-D DOA estimation with imperfect L-shaped array using active calibration," *IEEE Commun. Lett.*, vol. 25, no. 4, pp. 1178–1182, Apr. 2021.
- <span id="page-10-6"></span>[\[26\]](#page-1-0) H. Huang, J. Yang, H. Huang, Y. Song, and G. Gui, "Deep learning for super-resolution channel estimation and DOA estimation based massive MIMO system," *IEEE Trans. Veh. Technol.*, vol. 67, no. 9, pp. 8549–8560, Sep. 2018.
- <span id="page-10-7"></span>[\[27\]](#page-1-0) H. Y. Lee, J. Cho, M. Kim, and H. Park, "DNN-based feature enhancement using DOA-constrained ICA for robust speech recognition," *IEEE Signal Process. Lett.*, vol. 23, no. 8, pp. 1091–1095, Aug. 2016.
- <span id="page-10-8"></span>[\[28\]](#page-1-0) T. N. T. Nguyen, W. Gan, R. Ranjan, and D. L. Jones, "Robust source counting and DOA estimation using spatial pseudo-spectrum and convolutional neural network," *IEEE/ACM Trans. Audio, Speech, Language Process.*, vol. 28, pp. 2626–2637, 2020.
- <span id="page-10-9"></span>[\[29\]](#page-1-1) Y. Yuan, S. Wu, M. Wu, and N. Yuan, "Unsupervised learning strategy for direction-of-arrival estimation network," *IEEE Signal Process. Lett.*, vol. 28, pp. 1450–1454, 2021.
- <span id="page-10-10"></span>[\[30\]](#page-1-2) L. Wu, Z. Liu, and Z. Huang, "Deep convolution network for direction of arrival estimation with sparse prior," *IEEE Signal Process. Lett.*, vol. 26, no. 11, pp. 1688–1692, Nov. 2019.
- <span id="page-10-11"></span>[\[31\]](#page-1-3) G. K. Papageorgiou, M. Sellathurai, and Y. C. Eldar, "Deep networks for direction-of-arrival estimation in low SNR," *IEEE Trans. Signal Process.*, vol. 69, pp. 3714–3729, 2021.
- <span id="page-10-12"></span>[\[32\]](#page-1-4) R. Akter, V.-S. Doan, T. Huynh-The, and D.-S. Kim, "RFDOA-Net: An efficient ConvNet for RF-based DOA estimation in UAV surveillance systems," *IEEE Trans. Veh. Technol.*, vol. 70, no. 11, pp. 12209–12214, Nov. 2021.
- <span id="page-10-13"></span>[\[33\]](#page-1-5) A. M. Ahmed, U. S. K. P. M. Thanthrige, A. E. Gamal, and A. Sezgin, "Deep learning for DOA estimation in MIMO radar systems via emulation of large antenna arrays," *IEEE Commun. Lett.*, vol. 25, no. 5, pp. 1559–1563, May 2021.
- <span id="page-10-14"></span>[\[34\]](#page-1-6) A. M. Elbir, "DeepMUSIC: Multiple signal classification via deep learning," *IEEE Sensors Lett.*, vol. 4, no. 4, pp. 1–4, Apr. 2020.
- <span id="page-10-15"></span>[\[35\]](#page-1-7) Z.-M. Liu, C. Zhang, and S. Y. Philip, "Direction-of-arrival estimation based on deep neural networks with robustness to array imperfections," *IEEE Trans. Antennas Propag.*, vol. 66, no. 12, pp. 7315–7327, Dec. 2018.
- <span id="page-10-16"></span>[\[36\]](#page-1-8) S. Chakrabarty and E. A. P. Habets, "Multi-speaker DOA estimation using deep convolutional networks trained with noise signals," *IEEE J. Sel. Topics Signal Process.*, vol. 13, no. 1, pp. 8–21, Mar. 2019.
- <span id="page-10-17"></span>[\[37\]](#page-3-2) P. Chen, Z. Chen, Z. Cao, and X. Wang, "A new atomic norm for DOA estimation with gain-phase errors," *IEEE Trans. Signal Process.*, vol. 68, pp. 4293–4306, 2020.
- <span id="page-10-18"></span>[\[38\]](#page-3-2) Q. Wang, X. Wang, T. Dou, H. Chen, and X. Wu, "Gridless superresolution DOA estimation with unknown mutual coupling," in *Proc. IEEE Int. Conf. Acoust., Speech Signal Process. (ICASSP)*, May 2019, pp. 4210–4214.
- <span id="page-10-19"></span>[\[39\]](#page-3-2) A. G. Raj and J. H. McClellan, "Single snapshot super-resolution DOA estimation for arbitrary array geometries," *IEEE Signal Process. Lett.*, vol. 26, no. 1, pp. 119–123, Jan. 2019.
- <span id="page-10-20"></span>[\[40\]](#page-3-3) Q. Gong, S. Ren, S. Zhong, and W. Wang, "DOA estimation using sparse array with gain-phase error based on a novel atomic norm," *Digit. Signal Process.*, vol. 120, Jan. 2022, Art. no. 103266.
- <span id="page-10-21"></span>[\[41\]](#page-3-4) W. Liao and A. Fannjiang, "MUSIC for single-snapshot spectral estimation: Stability and super-resolution," *Appl. Comput. Harmon. Anal.*, vol. 40, no. 1, pp. 33–67, Jan. 2016.

- <span id="page-10-22"></span>[\[42\]](#page-7-4) Z. Wei, W. Wang, F. Dong, and Q. Liu, "Gridless one-bit directionof-arrival estimation via atomic norm denoising," *IEEE Commun. Lett.*, vol. 24, no. 10, pp. 2177–2181, Oct. 2020.
- <span id="page-10-23"></span>[\[43\]](#page-7-4) Z. Yang and L. Xie, "Enhancing sparsity and resolution via reweighted atomic norm minimization," *IEEE Trans. Signal Process.*, vol. 64, no. 4, pp. 995–1006, Feb. 2016.
- <span id="page-10-24"></span>[\[44\]](#page-7-5) Z. Yang, C. Zhang, J. Deng, and W. Lu, "Orthonormal expansion ℓ1 minimization algorithms for compressed sensing," *IEEE Trans. Signal Process.*, vol. 59, no. 12, pp. 6285–6290, Dec. 2011.
- <span id="page-10-25"></span>[\[45\]](#page-7-5) Z. Tan, P. Yang, and A. Nehorai, "Joint sparse recovery method for compressed sensing with structured dictionary mismatches," *IEEE Trans. Signal Process.*, vol. 62, no. 19, pp. 4997–5008, Oct. 2014.
- <span id="page-10-26"></span>[\[46\]](#page-7-6) G. Yu and G. Sapiro, "Statistical compressed sensing of Gaussian mixture models," *IEEE Trans. Signal Process.*, vol. 59, no. 12, pp. 5842–5858, Dec. 2011.
- <span id="page-10-27"></span>[\[47\]](#page-8-2) K. Aghababaiyan, V. Shah-Mansouri, and B. Maham, "High-precision OMP-based direction of arrival estimation scheme for hybrid nonuniform array," *IEEE Commun. Lett.*, vol. 24, no. 2, pp. 354–357, Feb. 2020.
- <span id="page-10-28"></span>[\[48\]](#page-8-2) M. Lin et al., "Single sensor to estimate DOA with programmable metasurface," *IEEE Internet Things J.*, vol. 8, no. 12, pp. 10187–10197, Jun. 2021.
- <span id="page-10-29"></span>[\[49\]](#page-8-2) Y. Chen, W. Wang, Z. Wang, and B. Xia, "A source counting method using acoustic vector sensor based on sparse modeling of DOA histogram," *IEEE Signal Process. Lett.*, vol. 26, no. 1, pp. 69–73, Jan. 2019.
- <span id="page-10-30"></span>[\[50\]](#page-8-3) G. Izacard, S. Mohan, and C. Fernandez-Granda, "Data-driven estimation of sinusoid frequencies," in *Proc. Adv. Neural Inf. Process. Syst.*, vol. 32, 2019, pp. 5127–5137.

![](_page_10_Picture_33.jpeg)

Peng Chen (Senior Member, IEEE) received the B.E. and Ph.D. degrees from the School of Information Science and Engineering, Southeast University, Nanjing, China, in 2011 and 2017, respectively.

From March 2015 to April 2016, he was a Visiting Scholar with the Department of Electrical Engineering, Columbia University, New York, NY, USA. He is currently an Associate Professor with the State Key Laboratory of Millimeter Waves, Southeast University. He is currently a Jiangsu Province Outstanding Young Scientist. His research interests

include target localization, super-resolution reconstruction, and array signal processing.

Dr. Chen received the Best Paper Award at IEEE ICCCCEE in 2017 and the Best Presentation Award in 2022 (IEEE ICCC). He has served as the IEEE ICCC Session Chair. He was invited as a Keynote Speaker at the IEEE ICET in 2022. He was recognized as an Exemplary Reviewer of IEEE WIRELESS COMMUNICATIONS LETTERS in 2021.

![](_page_10_Picture_38.jpeg)

Zhimin Chen (Member, IEEE) received the Ph.D. degree in information and communication engineering from the School of Information Science and Engineering, Southeast University, Nanjing, China, in 2015.

Since 2015, she has been an Associate Professor at Shanghai Dianji University, Shanghai, China. From 2021, she was a Visiting Scholar at the Department of Electronic and Information Engineering, The Hong Kong Polytechnic University, Hong Kong. Her research interests include

array signal processing, vehicle communications, and millimeter-wave communications.

{11}------------------------------------------------

![](_page_11_Picture_2.jpeg)

Liang Liu (Senior Member, IEEE) received the B.Eng. degree from Tianjin University, Tianjin, China, in 2010, and the Ph.D. degree from the National University of Singapore, Singapore, in 2014.

From 2015 to 2017, he was a Post-Doctoral Fellow with the Department of Electrical and Computer Engineering, University of Toronto, Toronto, ON, Canada. From 2017 to 2018, he was a Research Fellow with the Department of Electrical and Computer Engineering, the National University of Singapore.

He is currently an Assistant Professor with the Department of Electrical and Electronic Engineering, The Hong Kong Polytechnic University. His research interests lie in the next generation of cellular technologies such as machine-type communications for the Internet of Things, integrated sensing, and communication.

He was a recipient of the 2021 IEEE Signal Processing Society Best Paper Award, the 2017 IEEE Signal Processing Society Young Author Best Paper Award, the Best Student Award of the 2022 IEEE International Conference on Acoustics, Speech, and Signal Processing (ICASSP), and the Best Paper Award of the 2011 International Conference on Wireless Communications and Signal Processing. He was recognized by Clarivate Analytics as a Highly Cited Researcher in 2018. He is an Editor of IEEE TRANSACTIONS ON WIRELESS COMMUNICATIONS. He was a Leading Guest Editor of *IEEE Wireless Communications* Special Issue on Massive Machine-Type Communications for the IoT. He is a coauthor of the book *Next Generation Multiple Access* (Wiley-IEEE Press).

![](_page_11_Picture_7.jpeg)

Yun Chen (Senior Member, IEEE) received the B.Sc. degree from UESTC, Chengdu, China, in 2000, and the Ph.D. degree from Fudan University, Shanghai, China, in 2007.

In 2007, she joined Fudan University, where she has been with the faculty since March 2008. She has been an Associate Professor with the State Key Laboratory of ASIC and Systems, Fudan University. She has published more than 60 articles in such international journals and conferences as IEEE ASSCC, IEEE TRANSACTIONS ON CIRCUITS AND

SYSTEMS I: REGULAR PAPERS, IEEE TRANSACTIONS ON COMMUNICA-TIONS, IEEE ASP-DAC, IEEE ICASSP, ICC, and ISCAS. She applied for more than 20 patents. Her research interests include baseband processing technologies for wireless communication and ultralow power FEC IC design.

Dr. Chen is a member of the Steering Committee of SIPS and the ASICON Technical Committee. She serves as a TPC Member for ASSCC. She serves as the Chair Secretary for the Shanghai Chapter of IEEE SSCS, and the Co-Chair for the Circuit System Division, the Chinese Institute of Electronics.

![](_page_11_Picture_12.jpeg)

Xianbin Wang (Fellow, IEEE) received the Ph.D. degree in electrical and computer engineering from the National University of Singapore, Singapore, in 2001.

From January 2001 to July 2002, he was a System Designer with STMicroelectronics, where he was responsible for the system design of DSL and Gigabit Ethernet chipsets. He is currently a Professor and the Tier-I Canada Research Chair at Western University, London, ON, Canada. Before joining Western University, he was with the Communica-

tions Research Centre (CRC) Canada, Nepean, ON, Canada, as a Research Scientist/Senior Research Scientist, from July 2002 to December 2007. He has over 300 peer-reviewed journal and conference papers, in addition to 26 granted and pending patents and several standard contributions. His current research interests include 5G technologies, the Internet of Things, communications security, machine learning, and location technologies.

Dr. Wang is a fellow of the Canadian Academy of Engineering and an IEEE Distinguished Lecturer. He has received many awards and recognitions, including the Canada Research Chair, the CRC Presidents Excellence Award, the Canadian Federal Government Public Service Award, the Ontario Early Researcher Award, and five IEEE Best Paper Awards. He currently serves as an Editor/an Associate Editor for IEEE TRANSACTIONS ON COMMUNICATIONS, IEEE TRANSACTIONS ON BROADCASTING, and IEEE TRANSACTIONS ON VEHICULAR TECHNOLOGY and he was also an Associate Editor for IEEE TRANSACTIONS ON WIRELESS COMMUNICATIONS from 2007 to 2011, and IEEE WIRELESS COMMUNICATIONS LETTERS from 2011 to 2016. He was involved in many IEEE conferences including GLOBECOM, ICC, VTC, PIMRC, WCNC, and CWIT, in different roles such as symposium chair, tutorial instructor, track chair, session chair, and TPC co-chair.