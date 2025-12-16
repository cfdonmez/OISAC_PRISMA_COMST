

{0}------------------------------------------------

# Optical Integrated Sensing and Communication for Cooperative Mobile Robotics: Design and Experiments

Shengqian Wang<sup>1</sup> and He (Henry) Chen1, 2

<sup>1</sup>Department of Information Engineering, The Chinese University of Hong Kong, Hong Kong SAR, China <sup>2</sup>Shun Hing Institute of Advanced Engineering, The Chinese University of Hong Kong, Hong Kong SAR, China

*Abstract*—Integrated Sensing and Communication (ISAC) is an emerging technology that integrates wireless sensing and communication into a single system, transforming many applications, including cooperative mobile robotics. However, in scenarios where radio communications are unavailable, alternative approaches are needed. In this paper, we propose a new optical ISAC (OISAC) scheme for cooperative mobile robots by integrating camera sensing and screen-camera communication (SCC). Unlike previous throughput-oriented SCC designs that work with stationary SCC links, our OISAC scheme is designed for real-time control of mobile robots. It addresses new challenges such as image blur and long image display delay. As a case study, we consider the leader-follower formation control problem, an essential part of cooperative mobile robotics. The proposed OISAC scheme enables the follower robot to simultaneously acquire the information shared by the leader and sense the relative pose to the leader using only RGB images captured by its onboard camera. We then design a new control law that can leverage all the information acquired by the camera to achieve stable and accurate formations. We design and conduct realworld experiments involving uniform and nonuniform motions to evaluate the proposed system and demonstrate the advantages of applying OISAC over a benchmark approach that uses extended Kalman filtering (EKF) to estimate the leader's states. Our results show that the proposed OISAC-augmented leaderfollower formation system achieves better performance in terms of accuracy, stability, and robustness.

# I. INTRODUCTION

In recent years, cooperative mobile robotics has played an increasingly important role in a wide range of industrial applications, including cooperative transportation [1], exploration [2], and surveillance [3]. This technology offers promising performance, high efficiency, and effectiveness for operations that are dangerous or labor-intensive for humans [4]–[6]. Information perception and sharing using onboard sensors and wireless communications are crucial for cooperative robots to complete tasks, but traditionally, sensing and communications have been performed separately. However, the development of massive multi-input multi-output (MIMO) and millimeter wave (mmWave)/terahertz (THz) technologies has enabled the integration of sensing and wireless communications in shared hardware and spectrum resources [7]–[10]. Integrated Sensing and Communication (ISAC) offers new services and potential solutions for cooperative mobile robotics to address bottleneck

This research was supported in part by project #MMT 79/22 of the Shun Hing Institute of Advanced Engineering, The Chinese University of Hong Kong. The work of S. Wang was supported by the Hong Kong PhD Fellowship Scheme (PF20-48158).

Email:{ws021, he.chen}@ie.cuhk.edu.hk

![](_page_0_Picture_8.jpeg)

Fig. 1: Experimental setup. (a) Two Turtlebot2. (b) An illustrative feature image displayed on a 15.6-inch LCD screen.

challenges such as high-accuracy localization and tracking [10] and achieve better performance.

Reliable radio communications have been the mainstay of current ISAC designs. However, radio-based solutions can be severely impacted in the presence of radio interference, radio attacks or in scenarios unsuitable for radio propagation, such as underwater environments [11] and some military environments [12]. In such cases, radio-based solutions can have severely degraded performance or even lose functionality. As a result, many cooperative mobile robotics researchers are shifting their focus towards designing radio-free or sensingonly approaches to eliminate the dependence on radio communications [13]–[15]. Low-cost cameras are a preferable alternative to expensive sensors such as LiDAR, and camera sensing has been widely used in various cooperative mobile robotics applications supported by well-developed computer vision technologies [16]–[18]. However, the absence of communication inevitably leads to a decline in performance and application limitations of cooperative robot systems, despite tremendous efforts being spent on advanced and complicated sensing technologies to make up for it. In this context, inspired by radio ISAC, it is natural to ask *whether it is possible to design an optical ISAC (OISAC) scheme for cooperative mobile robotics that integrates camera sensing and optical communications in a single optical channel*. This would enable robots to simultaneously perceive and receive information using only low-cost cameras, maximizing the usage of optical channels. Such a system could help overcome the limitations of radio communications and provide a more reliable and costeffective solution for cooperative mobile robotics.

As an initial effort to answer the question above, this paper

{1}------------------------------------------------

develops a new robot operating system (ROS)-compatible OISAC scheme for cooperative mobile robotics that seamlessly integrates camera sensing and screen-camera communication (SCC). Our choice to make the OISAC scheme compatible with ROS was motivated by the fact that ROS has become the de facto software platform for robot design and programming. We choose the vision-based leader-follower formation control problem as our case study to evaluate the gain of the proposed OISAC scheme, since it represents a typical problem in cooperative mobile robotics. Most recent vision-based leader-follower formation control research has been based on camera sensing technologies, such as extended Kalman filtering (EKF) and high-gain observer-based output feedback algorithms that use observation of particular markers fixed on the leader to estimate its states, see e.g., [19]–[21] and references therein. However, we realized that because of no information communication, previous camera sensing-only methods may make the follower less agile to the dynamic changes of the leader's movements, which has been confirmed by experiments presented in Sec. IV. On the other hand, SCC is a form of optical camera communication technology that uses a screen to display images with data encoded in certain visual patterns, and a camera to capture the images and subsequently decode the embedded data [22]–[24]. We propose to integrate camera sensing and SCC so that both sensing and communication can be realized over one optical link and thus the follower can become more responsive to the changes of the leader's movements. Nevertheless, existing SCC frameworks designed for static optical links become no longer applicable in the considered application involving robot movements and delay-sensitive control.

The main contributions of this paper are three-fold: *Firstly*, we develop a new ROS-compatible OISAC scheme using only RGB images, in which a commodity LCD screen is mounted on the leader robot to display visual information, while a lowcost camera is fixed onboard the follower robot to capture RGB images. We carefully design the displayed images on the screen to realize sensing and communication through the same optical channel. We also propose new algorithms to combat the image blur caused by robot shaking and reduce the long image display delay. *Secondly*, we design and implement a new vision-based leader-follower formation system using our OISAC scheme, which enables the follower to simultaneously receive the leader's latest velocity and sense its relative pose to the leader. To leverage all the information acquired by the camera to achieve stable and accurate formation, we devise a new leader-follower formation controller with low computational complexity. The stability of our controller is proven by the Lyapunov stability theory [25]. Our OISACbased design enables the follower to react more agilely to the leader's dynamic movements. This is because directly reading out the leader's latest velocity from the captured images is far more accurate and up-to-date than any estimation, eliminating the need for complicated estimation algorithms. *Thirdly*, we design and conduct several real-world experiments involving uniform and nonuniform motions to evaluate the formation

![](_page_1_Picture_2.jpeg)

Fig. 2: Block diagram of our ROS-compatible OISAC.

performance of our system. Experimental results show that our system performs considerably better than a benchmark system that uses EKF to estimate the leader's states.

# II. DESIGN OF ROS-COMPATIBLE OISAC SCHEME

In this section, we present our design of the ROS-compatible OISAC scheme. This scheme incorporates two parts: the camera sensing part, which estimates the relative pose between two robots, and the communication part implemented by SCC, which enables the leader to send its states to the follower. The block diagram of the proposed OISAC is shown in Fig. 2. It is worth noting that existing SCC technologies designed for static scenarios may not function correctly on mobile robots with their default setups, as confirmed by our later experiments. Therefore, we will discuss the new problems posed by the considered mobile scenario and provide our solutions for overcoming them.

## *A. Screen-Camera Link Design*

This subsection elaborates on the design and implementation of a screen-camera link to realize OISAC, which can be used to boost the cooperative performance of mobile robots.

On the transmitter side, a commodity LCD screen is used to display visual information, and it continuously displays specific images, each containing a pixel matrix that carries data surrounded by four distinctive squares and white stripes, as illustrated in Fig. 1(b). Each square is considered a feature marker, and as we will explain later, the detection of these markers will be used for both camera sensing and pixel matrix extraction. Considering that objects with similar graphic features to the markers may exist in the background environments, we add a special graphic pattern (i.e., the black and white stripes) between the feature markers to enhance the detection accuracy. As shown in Fig. 2, the transmitted information is modulated into a two-dimensional (2-D) pixel matrix through a similar encoding and 2-D inverse Fourier Transform (IFFT) procedure presented in [22]. Meanwhile, each data bit is expanded by being interpolated with duplicate ones for high reliability. In our design, the first 4 bits are duplicated 5 times each and the second 4 bits are duplicated 3 times each.

At the receiver side, a low-cost camera is fixed onboard the follower to capture RGB images, and we extract the information conveyed by the RGB images to enhance the control performance. To that end, an edge detection algorithm is applied to recognize and locate four feature markers.

{2}------------------------------------------------

TABLE I: Packet loss rate under different distances.

| Distance (cm)    | 50    | 60    | 70    | 80    | 90    | 100   |
|------------------|-------|-------|-------|-------|-------|-------|
| Packet Loss Rate | 0.005 | 0.006 | 0.007 | 0.008 | 0.010 | 0.011 |
| Distance (cm)    | 110   | 120   | 130   | 140   | 150   |       |
| Packet Loss Rate | 0.017 | 0.028 | 0.057 | 0.102 | 0.357 |       |

TABLE II: Packet loss rate under different view angles.

| View Angle (degree) | 0    | 10   | 20 | 30 | 40   | 50   |
|---------------------|------|------|----|----|------|------|
| Packet Loss Rate    | 0.7% | 0.8% | 1% | 1% | 1.1% | 1.3% |

Specifically, we first convert each received image to a binary one and then apply the Canny edge detection algorithm [26] to extract graphic edges in the image and choose the edges with multi-hierarchy structure as potential candidates of the feature markers. The four feature markers are detected by verifying whether the pixels between the centers of each two candidates satisfy the predefined graphic pattern, where the centers of the markers are regarded as the feature points. The pixel coordinates of the feature points in the image can be used for camera sensing, i.e., relative pose estimation, which will be covered in Sec. III-D. Moreover, other information, such as the transmitter's velocity, can also be sensed or estimated using various techniques like EKF and nonlinear velocity estimation [19], [21]. On the other hand, the detection of the four feature points also contributes to SCC, as shown in Fig. 2. In practice, perspective distortion always exists in the received images since the screen and the camera can not be perfectly aligned. With the pixel coordinates of feature points, we conduct perspective transformation to correct the distortion so that the pixel matrix can be located and restored. To extract the information embedded in the pixel matrix, we apply demodulation and decoding operations in reverse to the aforementioned encoding and modulation process.

We conducted a series of experiments to evaluate the effects of distance and view angle on packet loss rates of the implemented SCC, where a low-cost Kinect camera and a 15.6-inch ThinkVision M14d monitor were used. The results are given in Table. I and II, which show that our screen-camera link design has a packet loss rate of less than 3% within 1.2-meter distance and 50-degree view angle. We note that trade-offs exist between screen size and OISAC performance, as well as between sensing performance and communication performance. First, the larger screen size, the easier for the receiver to sense the feature points and decode the information bits. As such, the screen-camera link is able to achieve lower packet loss rate at longer distance and larger view angle. Nevertheless, a larger screen requires higher power consumption. Moreover, when considering a fixed screen size, a larger sensing area consisting of four feature markers and white stripes can enhance the sensing capability and accuracy. However, this also results in compressed data area (pixel matrix), which can lead to lower throughput and higher packet loss rates. To strike an optimal balance, it is essential to consider the specific requirements of the application at hand.

## *B. Problems in Implementing OISAC for Mobile Robots*

The application of OISAC on mobile robots was not straightforward, and we encountered two main problems in our experiments: 1) image blur caused by robot shaking, and 2) long image display delays. In this subsection, we will describe the problems we encountered and present our solutions to enable the application of OISAC on mobile robots.

Mobile robots often experience shaking due to mechanical constraints, especially when they start or change their velocity. This shaking can cause severe blurring of the images captured by onboard cameras, ultimately leading to failed sensing and communication. For instance, in our study case of a leaderfollower formation control problem, the follower robot may fail to start moving at the beginning due to body shaking, which causes the captured images to be severely blurred, making it impossible for the follower to sense or receive any information, thus stopping immediately. In such cases, the follower may get caught in a starting-stopping cycle and shake violently in place, causing the formation to fail. To mitigate this problem, we have implemented a velocity smoothing process to prevent drastic changes in the robots' velocity. Taking inspiration from the keyboard teleop node in ROS, our velocity smoothing process involves constraining the robots' acceleration. Specifically, we denote u <sup>t</sup> = [v t , ω<sup>t</sup> T as the target velocity produced by the underlying control law, and u <sup>c</sup> = [v c , ω<sup>c</sup> T as the actual velocity of the robots. We then apply the following constraint:

$$\mathbf{u}_{i}^{c}(t) = \begin{cases} \min\{\mathbf{u}_{i}^{t}(t), \mathbf{u}_{i}^{c}(t-\delta_{t}) + \mathbf{a}_{i}\delta_{t}\}, \mathbf{u}_{i}^{t}(t) > \mathbf{u}_{i}^{c}(t-\delta_{t}), \\ \max\{\mathbf{u}_{i}^{t}(t), \mathbf{u}_{i}^{c}(t-\delta_{t}) - \mathbf{a}_{i}\delta_{t}\}, \mathbf{u}_{i}^{t}(t) \leq \mathbf{u}_{i}^{c}(t-\delta_{t}), \end{cases}$$

$$i = 1, 2.$$
(1)

Here, f<sup>v</sup> = 1/δ<sup>t</sup> denotes the publishing frequency of the velocity topic in ROS, and a = [ ˙vdes, ω˙ des] T represents the absolute value of the desired acceleration. This process ensures steady movements, which significantly improves the quality of the received images. Additionally, it offers the advantage that if the receiver experiences bit errors and obtains incorrect information, the actual control signals will not change sharply, ensuring the overall system's robustness.

Apart from image blur, image display delay at the transmitter is another problematic issue. For example, in our experiments we found that the information displayed on the screen may be outdated. In existing throughput-oriented SCC designs, image display delay is not a major concern as they only focus on the number of packets received within a given duration and do not consider how stale the received packets are. However, in our screen-camera link, delay-sensitivity is crucial as real-time control is critical in collaborative mobile robotics applications. In ROS, messages are exchanged in the form of topics, and communications are achieved through topic publishing and subscribing under ROS protocols. In our case, ROS nodes at the transmitter side publish topics on leader's states at a specific frequency, fpub. The SCC transmitter node subscribes to the topic with a custom-sized queue of size N<sup>q</sup>

{3}------------------------------------------------

TABLE III: Display delays under different queue sizes.

| Queue Size        | 1    | 10   | 20   | 30   | 40   | 50   |
|-------------------|------|------|------|------|------|------|
| Average Delay (s) | 0.06 | 0.67 | 1.38 | 2.03 | 2.55 | 3.21 |

and transforms the topics in the queue into displayed images. Assuming the time interval between the moment when the transmitter node receives its subscribed topic and when it displays the image embedding the topic information is  $T_{tx}$ , which mainly depends on the CPU's power and the size of the displayed image. If  $f_{pub} > 1/T_{tx}$ , indicating that the publishing frequency is higher than the image update frequency, the subscribing queue will be fully stacked, and the displayed images will be stale. We tested image display delays under different subscribing queue sizes, where the transmitter was running navigation with  $f_{pub} = 20$  Hz,  $T_{tx} = 60$  ms and displaying its current velocity information. As shown in Table III, the display delay substantially increases as the subscribing queue size increases, which can significantly impact system performance. To achieve real-time communication and control, we set  $N_q = 1$  by considering the fact that the follower is more concerned about the leader's latest states. In this sense, the image waiting to be displayed will be replaced by a newly generated image that incorporates fresher states of the leader.

### III. CASE STUDY: VISION-BASED LEADER-FOLLOWER FORMATION CONTROL

This section covers the leader-follower kinematics, camera model, visibility constraints, and problem formulation before detailing the relative pose estimation via camera sensing and the proposed control law.

# A. Leader-Follower Kinematics

As depicted in Fig. 3(a), we consider a vision-based leaderfollower system consisting of two nonholonomic mobile robots  $R_l$  and  $R_f$ , termed the leader and the follower, respectively. The follower is controlled to maintain a predefined relative pose to the leader based on the observations of the latter in its camera. The kinematics of each robot with respect to the world frame W can be written as

$$\begin{bmatrix} \dot{x}_i \\ \dot{y}_i \\ \dot{\theta}_i \end{bmatrix} = \begin{bmatrix} \cos \theta_i & 0 \\ \sin \theta_i & 0 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} v_i \\ \omega_i \end{bmatrix}, \tag{2}$$

where  $i \in \{l, f\}$  refers to the leader or the follower,  $\mathbf{r}_i =$  $[x_i, y_i]^T$  and  $\theta_i$  characterize the position and the orientation of robot  $R_i$  in the world frame  $\mathcal{W}$ , and  $\mathbf{u}_i = [v_i, \omega_i]^T$  is the control input of robot  $R_i$ , including the linear velocity  $v_i$  and the angular velocity  $\omega_i$ .

Define the position of the leader  $R_l$  with respect to the follower frame  $\mathcal{F}$  as  $\mathbf{r}_l^f = [x_l^f, y_l^f]^T$  to mathematically describe their relative position. We then have

$$\mathbf{r}_{l}^{f} = \begin{bmatrix} \cos \theta_{f} & \sin \theta_{f} \\ -\sin \theta_{f} & \cos \theta_{f} \end{bmatrix} (\mathbf{r}_{l} - \mathbf{r}_{f}). \tag{3}$$

![](_page_3_Picture_11.jpeg)

Fig. 3: (a) Leader-follower setup. (b) Camera model.

The time derivative of 
$$\mathbf{r}_{l}^{f}$$
 is
$$\dot{\mathbf{r}}_{l}^{f} = \begin{bmatrix} \dot{x}_{l}^{f} \\ \dot{y}_{l}^{f} \end{bmatrix} = \begin{bmatrix} v_{l} \cos \gamma \\ v_{l} \sin \gamma \end{bmatrix} + \begin{bmatrix} -1 & y_{l}^{f} \\ 0 & -x_{l}^{f} \end{bmatrix} \begin{bmatrix} v_{f} \\ \omega_{f} \end{bmatrix}, \quad (4)$$

where  $\gamma = \theta_l - \theta_f$  is the relative orientation between  $R_l$  and  $R_f$  satisfying  $\dot{\gamma} = \omega_l - \omega_f$ . According to (4) and the definitions of  $\gamma$  and  $\dot{\gamma}$ , the leader-follower kinematics can be expressed as:

$$\dot{\mathbf{s}} = \begin{bmatrix} \dot{x}_l^f \\ \dot{y}_l^f \\ \dot{\gamma} \end{bmatrix} = \begin{bmatrix} \cos \gamma & 0 \\ \sin \gamma & 0 \\ 0 & 1 \end{bmatrix} \mathbf{u}_l + \begin{bmatrix} -1 & y_l^f \\ 0 & -x_l^f \\ 0 & -1 \end{bmatrix} \mathbf{u}_f,$$

$$= \mathbf{F} \mathbf{u}_l + \mathbf{G} \mathbf{u}_f.$$
(5)

where  $\mathbf{s} = [x_l^f, y_l^f, \gamma]^T$  represents the relative pose between  $R_l$  and  $R_f$ , and  $\mathbf{u}_l = [v_l, \omega_l]^T$  and  $\mathbf{u}_f = [v_f, \omega_f]^T$  are the control inputs of  $R_l$  and  $R_f$ , respectively.

### B. Problem Statement

Given a desired relative pose  $\bar{\mathbf{s}} = [\bar{x}_l^f, \bar{y}_l^f, \bar{\gamma}]^T$ , the objective is to design a controller for the follower so that the relative pose  $\mathbf{s} = [x_l^f, y_l^f, \gamma]^T$  converges to an arbitrarily small neighborhood of the predefined  $\bar{s}$ . Furthermore, the following assumptions are made in this paper for practical purposes.

Assumption 1: The velocity and acceleration of the leader are bounded due to both mechanical constraints and visibility constraints, i.e.,

$$|v_l| \le v_{\text{max}}, \ |\omega_l| \le \omega_{\text{max}}, \ |\dot{v}_l| \le \dot{v}_{\text{max}}, \ |\dot{\omega}_l| \le \dot{\omega}_{\text{max}}.$$
 (6)

Assumption 2: The leader is visible to the follower at the initial stage, and all feature points onboard the leader are detectable initially.

Assumption 3: The relative orientation  $\gamma$  is bounded to ensure that all feature points can be identified in the presence of perspective distortion, i.e.,  $|\gamma| < \gamma_{\text{max}} < \frac{\pi}{2}$ .

#### C. Camera Model and Visibility Maintenance

The camera mounted onboard the follower often has limited field of view (FoV). Assume that the optical axis of the camera is aligned with the forward direction of the follower, as shown in Fig. 3(b). The pinhole camera model is used to project a 3-D point  $\mathbf{r}_Q^c = [x_Q^c, y_Q^c, z_Q^c]^T$  in the camera frame to the image plane of the camera with coordinates  $\mathbf{p}_Q^i = [m_Q, n_Q]^T$ . The perspective projection is given by

$$m_Q = f_m x_O^c / z_O^c + m_0, \quad n_Q = f_n y_O^c / z_O^c + n_0, \quad (7)$$

{4}------------------------------------------------

where  $f_m$  and  $f_n$  are pixel scaling factors;  $(m_0, n_0)$  is the image coordinates of the camera's principal point.

Since the camera has limited visual capability, the leader is visible to the follower only if the leader is within the follower's FoV. Assume that the visible region of the follower is a cone whose centerline coincides with the optical axis of the camera, as shown in the green dashed area in the Fig. 3(a). Define  $\alpha=\arctan(y_l^f/x_l^f)$  as the bearing angle of the leader's center with respect to the follower frame, and  $\alpha_{\rm max}$  and  $d_{\rm max}$  as the maximum angle and distance of view, respectively. To maintain the visual observation of the leader in the FoV of the follower, the following conditions should be satisfied:

$$2\mu \cos\left(\alpha_{\max} - \frac{\pi}{6}\right) < x_l^f \le d_{\max} - \mu,$$

$$|\alpha| \le \arctan\left(\frac{x_l^f \sin \alpha_{\max} - \mu}{x_l^f \cos \alpha_{\max}}\right),$$
(8)

where  $\mu$  is the collision radius of the leader.

In our study case, we use the OISAC scheme to transmit the leader's velocity information to the follower. Define  $\hat{\mathbf{u}}_l = [\hat{v}_l, \hat{\omega}_l]^T$  as the obtained velocity information from the SCC link, and  $\boldsymbol{\delta} = [\delta_v, \delta_\omega]^T = [v_l - \hat{v}_l, \omega_l - \hat{\omega}_l]^T$  as the error between  $\mathbf{u}_l$  and  $\hat{\mathbf{u}}_l$ . Normally  $\boldsymbol{\delta}$  is bounded by the quantization error  $[v_{max}/2^{n+1}, \omega_{max}/2^{n+1}]^T$ , where the number of bits is set to n=8 in this paper. With the acceleration constraints described in (6),  $\hat{\mathbf{u}}_l$  should not change drastically in a short time interval  $\Delta t$ . We thus have

$$|\hat{v}_l(t) - \hat{v}_l(t - \triangle t)| \le N\dot{v}_{des}\triangle t,\tag{9}$$

$$|\hat{\omega}_l(t) - \hat{\omega}_l(t - \triangle t)| \le N\dot{\omega}_{des}\triangle t,\tag{10}$$

where N is a positive integer. In case  $\hat{\mathbf{u}}_l(t)$  does not satisfy the acceleration constraints (9)-(10), or the feature points are not detected correctly, the corresponding visual information captured in the previous sampling interval will be applied. This verification process implies that  $\boldsymbol{\delta}$  is bounded by

$$\delta_v = |v_l - \hat{v}_l| \le \delta_v^+ = \max\left\{\frac{v_{max}}{2^{n+1}}, N\dot{v}_{des}\triangle t\right\},\tag{11}$$

$$\delta_{\omega} = |\omega_l - \hat{\omega}_l| \le \delta_{\omega}^+ = \max\left\{\frac{\omega_{max}}{2^{n+1}}, N\dot{\omega}_{des}\triangle t\right\}.$$
 (12)

where the period interval  $\triangle t$  is chosen to be 100ms. Furthermore, substituting (6) into (11)-(12) yields

$$|\hat{v}_l| \le \hat{v}_l^+ = v_{max} + N\dot{v}_{des}\triangle t,\tag{13}$$

$$|\hat{\omega}_l| \le \hat{\omega}_l^+ = \omega_{max} + N\dot{\omega}_{des} \triangle t. \tag{14}$$

#### D. Camera Sensing: Relative Pose Estimation

We now describe our camera sensing method for the follower to estimate the relative pose from the leader using only the RGB images captured by the onboard camera. In most vision-based leader-follower formation control methods, typically the leader is equipped with particular markers so that the follower can position them in the camera. Here our markers are the aforementioned four feature points displayed on the screen.

Assume that the plane of the screen is perpendicular to the forward direction of the leader, and the four feature points

![](_page_4_Picture_16.jpeg)

Fig. 4: Pose estimation.

form a rectangle. The camera onboard the follower satisfies the pinhole camera model discussed in Sec. III-C. As shown in Fig. 4, we assume that the horizontal distance between the origin of the follower frame and the camera's principal point is  $d_f$ , and the horizontal distance between the origin of the leader frame and the LCD screen is  $d_l$ . The feature points are horizontally separated by  $L_1$  and vertically separated by  $L_2$ . Both robots have a prior knowledge of  $d_f$ ,  $d_l$ ,  $L_1$  and  $L_2$ . From the observation of the camera, the pixel coordinates of the feature points A, B, C and D in the image plane are denoted by  $\mathbf{p}_{A}^{i} = [m_{A}, n_{A}]^{T}$ ,  $\mathbf{p}_{B}^{i} = [m_{B}, n_{B}]^{T}$ ,  $\mathbf{p}_{C}^{i} = [m_{C}, n_{C}]^{T}$ ,  $\mathbf{p}_{D}^{i} = [m_{D}, n_{D}]^{T}$ , respectively. Define  $\widetilde{m}_{j} = m_{j} - m_{0}$ ,  $\widetilde{n}_{j} = m_{j} - m_{0}$ ,  $\widetilde{n}_{j} = m_{j} - m_{0}$ ,  $\widetilde{n}_{j} = m_{j} - m_{0}$ ,  $\widetilde{n}_{j} = m_{j} - m_{0}$ ,  $\widetilde{n}_{j} = m_{j} - m_{0}$ ,  $\widetilde{n}_{j} = m_{j} - m_{0}$ ,  $\widetilde{n}_{j} = m_{j} - m_{0}$ ,  $\widetilde{n}_{j} = m_{j} - m_{0}$ ,  $\widetilde{n}_{j} = m_{j} - m_{0}$ ,  $\widetilde{n}_{j} = m_{j} - m_{0}$ ,  $\widetilde{n}_{j} = m_{j} - m_{0}$ ,  $\widetilde{n}_{j} = m_{j} - m_{0}$ ,  $\widetilde{n}_{j} = m_{j} - m_{0}$ ,  $\widetilde{n}_{j} = m_{j} - m_{0}$ ,  $\widetilde{n}_{j} = m_{j} - m_{0}$ ,  $\widetilde{n}_{j} = m_{j} - m_{0}$ ,  $\widetilde{n}_{j} = m_{j} - m_{0}$ ,  $\widetilde{n}_{j} = m_{j} - m_{0}$ ,  $\widetilde{n}_{j} = m_{j} - m_{0}$ ,  $\widetilde{n}_{j} = m_{j} - m_{0}$ ,  $\widetilde{n}_{j} = m_{j} - m_{0}$ ,  $\widetilde{n}_{j} = m_{j} - m_{0}$ ,  $\widetilde{n}_{j} = m_{j} - m_{0}$ ,  $\widetilde{n}_{j} = m_{j} - m_{0}$ ,  $\widetilde{n}_{j} = m_{j} - m_{0}$ ,  $\widetilde{n}_{j} = m_{j} - m_{0}$ ,  $\widetilde{n}_{j} = m_{j} - m_{0}$ ,  $\widetilde{n}_{j} = m_{j} - m_{0}$ ,  $\widetilde{n}_{j} = m_{j} - m_{0}$ ,  $\widetilde{n}_{j} = m_{j} - m_{0}$ ,  $\widetilde{n}_{j} = m_{j} - m_{0}$ ,  $\widetilde{n}_{j} = m_{j} - m_{0}$ ,  $\widetilde{n}_{j} = m_{j} - m_{0}$ ,  $\widetilde{n}_{j} = m_{j} - m_{0}$ ,  $\widetilde{n}_{j} = m_{j} - m_{0}$ ,  $\widetilde{n}_{j} = m_{j} - m_{0}$ ,  $\widetilde{n}_{j} = m_{j} - m_{0}$ ,  $\widetilde{n}_{j} = m_{j} - m_{0}$ ,  $\widetilde{n}_{j} = m_{j} - m_{0}$ ,  $\widetilde{n}_{j} = m_{j} - m_{0}$ ,  $\widetilde{n}_{j} = m_{j} - m_{0}$ ,  $\widetilde{n}_{j} = m_{j} - m_{0}$ ,  $\widetilde{n}_{j} = m_{j} - m_{0}$ ,  $\widetilde{n}_{j} = m_{j} - m_{0}$ ,  $\widetilde{n}_{j} = m_{j} - m_{0}$ ,  $\widetilde{n}_{j} = m_{j} - m_{0}$ ,  $\widetilde{n}_{j} = m_{j} - m_{0}$ ,  $\widetilde{n}_{j} = m_{j} - m_{0}$ ,  $\widetilde{n}_{j} = m_{j} - m_{0}$ ,  $\widetilde{n}_{j} = m_{j} - m_{0}$ ,  $\widetilde{n}_{j} = m_{j} - m_{0}$ ,  $\widetilde{n}_{j} = m_{j} - m_{0}$ ,  $\widetilde{n}_{j} = m_{j} - m_{0}$ ,  $\widetilde{n}_{j} = m_{j} - m_{0}$ ,  $\widetilde{n}_{j} = m_{j} - m_{0}$ ,  $\widetilde{n}_{j} = m_{j} - m_{0}$ ,  $\widetilde{n}_{j} = m_{j} - m_{0}$ ,  $\widetilde{n}_{j} = m_{0} - m_{0}$ ,  $\widetilde{n}_{j} = m_{0} - m_{0}$  $n_i - n_0$ ,  $j = \{A, B, C, D\}$  as the pixel distances between the i-th pixel point and the origin of the image plane. Based on the pixel coordinates that can be directly acquired from the received RGB image, we can reconstruct the following coordinates  $(z_A^c, x_A^c)$  and  $(z_B^c, x_B^c)$  of feature points A and B in the camera frame, where

$$z_A^c = \frac{f_n L_2}{n_C - n_A}, \ z_B^c = \frac{f_n L_2 \widetilde{n_A}}{(n_C - n_A)\widetilde{n_B}},$$
 (15)

$$x_A^c = \frac{f_n L_2 \widetilde{m_A}}{f_m (n_C - n_A)}, \ x_B^c = \frac{f_n L_2 \widetilde{m_B} \widetilde{n_A}}{f_m (n_C - n_A) \widetilde{n_B}}.$$
 (16)

According to the following geometric relationship depicted in Fig. 4, the coordinates of the screen's center *O* in the camera frame can be derived as:

$$z_O^c = \frac{1}{2}(z_A^c + z_B^c) = \frac{f_n L_2(\widetilde{n_A} + \widetilde{n_B})}{2(n_C - n_A)\widetilde{n_B}},$$
(17)

$$x_O^c = \frac{1}{2}(x_A^c + x_B^c) = \frac{f_n L_2(\widetilde{m_A}\widetilde{n_B} + \widetilde{m_B}\widetilde{n_A})}{2f_m(n_C - n_A)\widetilde{n_B}}.$$
 (18)

The relative distance  $\mathbf{r}_l^f = [x_l^f, y_l^f]^T$  between the leader and the follower can then be estimated as:

$$x_l^f = z_O^c + d_f + d_l \cos \gamma, \tag{19}$$

$$y_l^f = -x_O^c + d_l \sin \gamma, \tag{20}$$

{5}------------------------------------------------

where the relative orientation  $\gamma$  satisfies

$$\sin \gamma = \frac{1}{L_1} (z_B^c - z_A^c) = \frac{f_n L_2(\widetilde{n_A} - \widetilde{n_B})}{L_1(n_C - n_A)\widetilde{n_B}},\tag{21}$$

$$\cos \gamma = \frac{1}{L_1} (x_B^c - x_A^c) = \frac{f_n L_2(\widetilde{m_B} \widetilde{n_A} - \widetilde{m_A} \widetilde{n_B})}{f_m L_1(n_C - n_A) \widetilde{n_B}}.$$
 (22)

#### E. Control Law

In this subsection, we devise a control law that can leverage the leader's velocity information and the relative pose extracted from the OISAC scheme to achieve a stable formation between the two robots.

Define the vector of formation errors as  $\boldsymbol{\varepsilon} = [\varepsilon_x, \varepsilon_y, \varepsilon_\gamma]^T = [x_l^f - \overline{x}_l^f, y_l^f - \overline{y}_l^f, \gamma - \overline{\gamma}]^T$ . To maintain a desired formation is equivalent to ensuring that  $\boldsymbol{\varepsilon}$  converges to an arbitrarily small neighborhood of  $\mathbf{0} \in \mathbb{R}^3$ . Recall that the time derivative of  $\boldsymbol{\varepsilon}$  has been given in (5). Define  $\sigma = 1/\left(\left(x_l^f\right)^2 + 1\right)$ . We propose the following control law:

$$\mathbf{u}_f = \begin{bmatrix} v_f \\ \omega_f \end{bmatrix} = \sigma \mathbf{H} (\mathbf{K} \boldsymbol{\varepsilon} + \mathbf{F} \hat{\mathbf{u}}_l), \tag{23}$$

where  $\mathbf{K} = \operatorname{diag}(k_1, k_2, k_3)$  contains three tunable positive scalars; recall that  $\hat{\mathbf{u}}_l = [\hat{v}_l, \hat{\omega}_l]^T$  is the velocity information captured by the follower using the vision scheme presented in Sec. II; the matrix  $\mathbf{H}$  is given by

$$\mathbf{H} = \begin{bmatrix} 1/\sigma & x_l^f y_l^f & y_l^f \\ 0 & x_l^f & 1 \end{bmatrix}. \tag{24}$$

We have the following theorem regarding the formation errors of the control law in (23):

**Theorem 1**: Considering a leader-follower system with the kinematics in (5) satisfying Assumptions 1-4 and the formation control law in (23), the prescribed stable formation performance in Sec. III-B can be achieved by properly selecting parameters  $k_1$ ,  $k_2$  and  $k_3$ . That is, the formation errors  $\varepsilon$  are bounded and have guaranteed convergences.

*Proof:* Consider the following Lyapunov candidate  $V = \varepsilon^T \varepsilon/2$ . Denote  $\eta = x_l^f \sigma$ . Substituting (5) and (23)-(24) into the Lyapunov candidate, we have its time derivative given by

$$\dot{V} = \boldsymbol{\varepsilon}^{T} \dot{\boldsymbol{\varepsilon}} = \boldsymbol{\varepsilon}^{T} [\mathbf{F} \mathbf{u}_{l} + \sigma \mathbf{G} \mathbf{H} (\mathbf{K} \boldsymbol{\varepsilon} + \mathbf{F} \hat{\mathbf{u}}_{l})], 
= -k_{1} \varepsilon_{x}^{2} - k_{2} \eta x_{l}^{f} \varepsilon_{y}^{2} - k_{3} \sigma \varepsilon_{\gamma}^{2} + \varepsilon_{x} (v_{l} - \hat{v}_{l}) \cos \gamma 
+ \varepsilon_{y} [(v_{l} - \eta x_{l}^{f} \hat{v}_{l}) \sin \gamma - \eta \hat{\omega}_{l} - \eta (k_{2} + k_{3}) \varepsilon_{\gamma}] 
+ \varepsilon_{\gamma} (\omega_{l} - \sigma \hat{\omega}_{l} - \eta \hat{v}_{l} \sin \gamma).$$
(25)

For clarity, we define

$$\xi_1 = (v_l - \hat{v}_l)\cos\gamma,\tag{26}$$

$$\xi_2 = (v_l - \eta x_l^f \hat{v}_l) \sin \gamma - \eta \hat{\omega}_l - \eta (k_2 + k_3) \varepsilon_{\gamma}, \tag{27}$$

$$\xi_3 = \omega_l - \sigma \hat{\omega}_l - \eta \hat{v}_l \sin \gamma. \tag{28}$$

Substituting (11)-(14) into (26)-(28) further yields

$$|\xi_1| \le \delta_v^+,\tag{29}$$

$$|\xi_{2}| \leq |v_{l} - \hat{v}_{l}| + |\sigma \hat{v}_{l}| + \eta[(k_{2} + k_{3})|\varepsilon_{\gamma}| + |\hat{\omega}_{l}|]$$
  
$$\leq \delta_{v}^{+} + \sigma \hat{v}_{l}^{+} + \eta[(k_{2} + k_{3})|\varepsilon_{y}| + \hat{\omega}_{l}^{+}], \tag{30}$$

$$|\xi_3| \le |\omega_l - \hat{\omega}_l| + |\eta x_l^f \hat{\omega}_l| + |\eta \hat{v}_l|$$
  
$$\le \delta_\omega^+ + \eta x_l^f \hat{\omega}_l^+ + \eta \hat{v}_l^+. \tag{31}$$

By properly choosing  $k_1$ ,  $k_2$  and  $k_3$  such that  $k_1 \geq 2\delta_v^+/|\varepsilon_x|$ ,  $k_2 \geq 2[\delta_v^+ + \sigma \hat{v}_l^+ + \eta(k_3|\varepsilon_y| + \hat{\omega}_l^+)]/(\eta(x_l^f + 1)|\varepsilon_y|)$ , and  $k_3 \geq 2(\delta_\omega^+ + \eta x_l^f \hat{\omega}_l^+ + \eta \hat{v}_l^+)/(\sigma|\varepsilon_\gamma|)$ , we can bound  $\dot{V}$  given in (25) as follows

$$\dot{V} \le -(k_1 \varepsilon_x^2 + k_2 \eta x_l^f \varepsilon_y^2 + k_3 \sigma \varepsilon_\gamma^2)/2 < -\phi \varepsilon^T \varepsilon/2 = -\phi V.$$
(32)

where  $\phi = \min\{k_1, k_2\eta x_l^f, k_3\sigma\}$ . According to the Lyapunov stability theory, (32) indicates that the proposed leader-follower system is asymptotically stable, and the error  $\varepsilon$  is bounded. This ends the proof.

#### IV. EXPERIMENTAL RESULTS

We conducted real-world experiments on two Turtlebot2 robots to evaluate the proposed formation system. In our experiments, the VICON motion capture system is used to obtain the positions of the mobile robots with respect to a global frame that are used as ground truth. The frequency of the VICON cameras is set to 100 frames per second (fps). We attached three reflective markers on the top layer of each robot forming an isosceles triangle so that the orientation of each robot can be determined by the coordinates of three markers. The follower is equipped with a Kinect camera to capture RGB images. Each robot is connected to an Intel NUC mini PC, running on Ubuntu 18.04. The vision algorithm and the proposed control law are implemented in robot operating system (ROS) Melodic. For robustness and practical purposes, the parameter settings are chosen as follows:  $d_{\text{max}} = 1.45 \text{m}$ ,  $\gamma_{\mathrm{max}} = \pi/3$ ,  $\alpha_{\mathrm{max}} = \pi/4$ , r = 0.2m,  $v_{\mathrm{max}} = 0.6$ m/s,  $\omega_{\text{max}} = 0.2 \text{rad/s}, \ \dot{v}_{\text{max}} = 0.5 \text{m/s}^2, \ \dot{\omega}_{\text{max}} = 0.2 \text{rad/s}^2,$  $k_1 = 0.5, k_2 = 0.75, k_3 = 0.5, N = 5, \Delta t = 100 \text{ms},$  $f_m = f_n = 500$ pixels/m,  $m_0 = 320$ pixels,  $n_0 = 240$ pixels,  $L_1 = 0.232 \text{m}, \ L_2 = 0.145 \text{m}, \ d_l = 0.275 \text{m}, \ d_f = -0.017 \text{m}.$ To evaluate the formation stability and robustness, we conducted the following three experiments: 1) formation along a straight/circular path with the velocity of the leader being constant; 2) braking distance when the leader sharply decelerates; 3) formation along a U-shaped path with velocity of the leader being time-varying.

The first experiment is designed to test the basic formation performance of the proposed scheme, where the leader's velocity is set to be constant. Due to space limitation, we only show the experimental results of the case with a circular path, though even better performance has been observed for the case with a straight path. In this experiment, the leader moves along a circular path with  $v_l = 0.125 \text{m/s}$  and  $\omega_l = 0.1 \text{rad/s}$ . The relative pose is initialized as  $\mathbf{s}_0 = [1.25, -0.3, 0]^T$ , and the desired one is set to  $\bar{\mathbf{s}} = [0.75, 0, \pi/6]^T$ . The experimental results are shown in Fig. 5. The trajectories recorded by the motion capture system are depicted in Fig. 5(a), where the circles mark the starting points and the squares mark the ending points. Figs. 5(b)-5(d) show that the formation errors quickly reduce and then varies within a small range, i.e.,  $\hat{\varepsilon} = [\pm 0.02, \pm 0.02, \pm 0.02]^T$ . The results indicate that the proposed scheme can achieve a stable and accurate formation under linear/circular motion with a constant velocity.

{6}------------------------------------------------

![](_page_6_Figure_0.jpeg)

![](_page_6_Figure_1.jpeg)

![](_page_6_Figure_2.jpeg)

![](_page_6_Figure_3.jpeg)

Fig. 5: Results of the first experiment. (a) Trajectory. (b)-(d) Formation errors.

![](_page_6_Figure_5.jpeg)

Fig. 6: Braking distance in the second experiment.

In order to demonstrate the merits of our proposed system, we designed experiments involving motions with dynamic velocity of the leader (i.e.,  $v_l$  may change). Specifically, in the second experiment, the leader executed a linear motion until the formation stabilizes, and then sharply braked with the maximum deceleration. This experiment can evaluate the follower's responsiveness to the leader's dynamic velocity. Thanks to the OISAC scheme developed in Sec. II, the follower is expected to react faster to the leader's deceleration to avoid significant formation errors or even a collision. We measured the braking distance of the follower at six levels of  $v_l$  from 0.1m/s to 0.6m/s. Additionally, we implemented the velocity estimation method using extended Kalman filtering (EKF) [27] to serve as the benchmark. For each level of  $v_l$ , 10 measurements are performed for both the proposed method and the benchmarking EKF method, totaling 120 measurements. We averaged the 10 measurement results for each  $v_l$  as the performance metric. The results are presented in Fig. 6. It can be clearly observed that compared with the follower using the EKF method, the follower based on the proposed vision scheme has much shorter braking distance (all not exceeding 0.08m), about  $3 \times$  to  $5 \times$  shorter than that of the benchmark. This is because our OISAC-augmented follower is more agile to the drastic changes of the leader's velocity, resulting in a more robust control law in nonuniform motions.

In the third experiment, the leader is designed to move along a U-shaped trajectory consisting of two straight trajectory sectors and a semicircular sector, as shown in Fig. 7(a), where the circles mark the starting points and the squares mark the ending points. The leader starts with a straight line at a velocity of  $\mathbf{u}_l = [0.3, 0]^T$ . When entering the semicircular sector, the leader changes its velocity to  $\mathbf{u}_l = [0.1, \frac{\pi}{30}]^T$ . After the semicircular sector is passed, the leader accelerates at a velocity of  $\mathbf{u}_l = [0.3, 0]^T$  to complete the last straight sector.

The moments when the leader crosses the two intersection points of the trajectory sectors are marked with black dotted lines in Figs. 7(b)-7(d). The relative pose is initialized as  $\mathbf{s}_0 = [0.9, 0.1, 0.31]^T$ . The desired relative pose is set to  $\overline{\mathbf{s}} = [0.6, 0, 0]^T$  during the linear motion, while it is switched to  $\overline{\mathbf{s}} = [0.6, 0.15, \frac{\pi}{6}]^T$  during the circular motion. We also implemented the benchmark scheme using EKF velocity estimation for comparison purposes. Since both schemes reconstruct the leader's velocity, the trajectory switches and the associated velocity changes can be perceived by the follower.

The experimental results of the third experiment are presented in Fig. 7. From Fig. 7(a), we can see that our follower achieves a smoother tracking trajectory when compared to the EKF-based scheme. Meanwhile, Figs. 7(b)-7(d) show that the formation errors in our system converge faster and is stabler. In particular, the formation error  $\varepsilon_x$  fluctuates much more gently when  $\mathbf{u}_l$  changes at the intersections of the trajectory sectors. In Figs. 7(e)-7(f) we can observe that the velocity received by the proposed follower matches well with the leader's actual velocity, while the EKF estimation has considerable delay and jitter. Overall, the results indicate that the proposed leader-follower system is more responsive to velocity changes.

#### V. CONCLUSIONS

In this paper, we developed a ROS-compatible OISAC scheme that integrates camera sensing and SCC for cooperative mobile robotics. Our scheme addresses new problems such as image blur and long image display delays, and is designed for real-time control of mobile robots. Our experiments have validated the functionality of the proposed scheme. We focused on the leader-follower formation control as a case study, and designed an OISAC-augmented control system that enables the follower to use RGB images to estimate the relative pose to the leader and extract the state information sent by the leader. We implemented a new control law with proven stability and bounded errors to achieve accurate and stable formation control. Real-world experiments using two Turtlebot2 robots demonstrated the stability and robustness of the proposed scheme, and showed that the follower using the OISAC scheme and the devised control law is more responsive to the leader's movements than a benchmark system that uses EKF to estimate the leader's states. Future work includes trying other optical communication technologies (e.g., visible light communication) and adapting the OISAC scheme to more

{7}------------------------------------------------

![](_page_7_Figure_0.jpeg)

Fig. 7: Results of the third experiment. (a) Trajectory. (b)-(d) Formation errors. (e)-(f) Actual velocity, received velocity and estimated velocity of the leader.

complex tasks, such as obstacle avoidance and cooperative object transportation.

# REFERENCES

- [1] T. Machado, T. Malheiro, S. Monteiro, W. Erlhagen, and E. Bicho, "Multi-constrained joint transportation tasks by teams of autonomous mobile robots using a dynamical systems approach," in *2016 IEEE international conference on robotics and automation (ICRA)*. IEEE, 2016, pp. 3111–3117.
- [2] Y. Yasuda, N. Kubota, and Y. Toda, "Adaptive formation behaviors of multi-robot for cooperative exploration," in *2012 IEEE International Conference on Fuzzy Systems*. IEEE, 2012, pp. 1–6.
- [3] A. M. Khaleghi, D. Xu, S. Minaeian, M. Li, Y. Yuan, J. Liu, Y.-J. Son, C. Vo, and J.-M. Lien, "A dddams-based uav and ugv team formation approach for surveillance and crowd control," in *Proceedings of the Winter Simulation Conference 2014*. IEEE, 2014, pp. 2907–2918.
- [4] R. G. Lins and S. N. Givigi, "Cooperative robotics and machine learning for smart manufacturing: platform design and trends within the context of industrial internet of things," *IEEE Access*, vol. 9, pp. 95 444–95 455, 2021.
- [5] M. Ronzoni, R. Accorsi, L. Botti, and R. Manzini, "A support-design framework for cooperative robots systems in labor-intensive manufacturing processes," *Journal of Manufacturing Systems*, vol. 61, pp. 646–657, 2021.
- [6] C. Lytridis, V. G. Kaburlasos, T. Pachidis, M. Manios, E. Vrochidou, T. Kalampokas, and S. Chatzistamatis, "An overview of cooperative robotics in agriculture," *Agronomy*, vol. 11, no. 9, p. 1818, 2021.
- [7] Y. Cui, F. Liu, X. Jing, and J. Mu, "Integrating sensing and communications for ubiquitous iot: Applications, trends, and challenges," *IEEE Network*, vol. 35, no. 5, pp. 158–167, 2021.
- [8] F. Liu, Y. Cui, C. Masouros, J. Xu, T. X. Han, Y. C. Eldar, and S. Buzzi, "Integrated sensing and communications: Towards dual-functional wireless networks for 6g and beyond," *IEEE journal on selected areas in communications*, 2022.

- [9] A. Liu, Z. Huang, M. Li, Y. Wan, W. Li, T. X. Han, C. Liu, R. Du, D. K. P. Tan, J. Lu *et al.*, "A survey on fundamental limits of integrated sensing and communication," *IEEE Communications Surveys & Tutorials*, vol. 24, no. 2, pp. 994–1034, 2022.
- [10] D. K. P. Tan, J. He, Y. Li, A. Bayesteh, Y. Chen, P. Zhu, and W. Tong, "Integrated sensing and communication in 6g: Motivations, use cases, requirements, challenges and future directions," in *2021 1st IEEE International Online Symposium on Joint Communications & Sensing (JC&S)*. IEEE, 2021, pp. 1–6.
- [11] X. Li, D. Zhu, and Y. Qian, "A survey on formation control algorithms for multi-auv system," *Unmanned Systems*, vol. 2, no. 04, pp. 351–359, 2014.
- [12] L. Lin, Z. Wang, H. Liang, F. Xu, and J. Huang, "A communication-free leader-follower formation method for ugvs via sensors fusion," in *2018 IEEE International Conference on Information and Automation (ICIA)*. IEEE, 2018, pp. 378–384.
- [13] A. Bautin, O. Simonin, and F. Charpillet, "Towards a communication free coordination for multi-robot exploration," in *6th National conference on control architectures of robots*, 2011, pp. 8–p.
- [14] S. T. Kalat, S. G. Faal, and C. D. Onal, "A decentralized, communication-free force distribution method with application to collective object manipulation," *Journal of Dynamic Systems, Measurement, and Control*, vol. 140, no. 9, p. 091012, 2018.
- [15] Y. Cai, G. Zhu, H. Huang, Z. Wang, Z. Fan, W. Li, Z. Shi, and W. Ning, "The behavior design of swarm robots based on a simplified gene regulatory network in communication-free environments," in *International Workshop on Advanced Computational Intelligence and Intelligent Informatics*, 2021.
- [16] A. Giusti, J. Nagi, L. Gambardella, and G. A. Di Caro, "Cooperative sensing and recognition by a swarm of mobile robots," in *2012 IEEE/RSJ International Conference on Intelligent Robots and Systems*. IEEE, 2012, pp. 551–558.
- [17] A. Khan, B. Rinner, and A. Cavallaro, "Cooperative robots to observe moving targets," *IEEE transactions on cybernetics*, vol. 48, no. 1, pp. 187–198, 2016.
- [18] H. Wang, D. Guo, X. Liang, W. Chen, G. Hu, and K. K. Leang, "Adaptive vision-based leader–follower formation control of mobile robots," *IEEE Transactions on Industrial Electronics*, vol. 64, no. 4, pp. 2893–2902, 2016.
- [19] G. L. Mariottini, F. Morbidi, D. Prattichizzo, G. J. Pappas, and K. Daniilidis, "Leader-follower formations: Uncalibrated vision-based localization and control," in *Proceedings 2007 IEEE International Conference on Robotics and Automation*. IEEE, 2007, pp. 2403–2408.
- [20] R. Tron, J. Thomas, G. Loianno, K. Daniilidis, and V. Kumar, "A distributed optimization framework for localization and formation control: Applications to vision-based measurements," *IEEE Control Systems Magazine*, vol. 36, no. 4, pp. 22–44, 2016.
- [21] N. Moshtagh, N. Michael, A. Jadbabaie, and K. Daniilidis, "Visionbased, distributed control laws for motion coordination of nonholonomic robots," *IEEE Transactions on Robotics*, vol. 25, no. 4, pp. 851–860, 2009.
- [22] S. D. Perli, N. Ahmed, and D. Katabi, "Pixnet: Interference-free wireless links using lcd-camera pairs," in *Proceedings of the sixteenth annual international conference on Mobile computing and networking*, 2010, pp. 137–148.
- [23] W. Hu, H. Gu, and Q. Pu, "Lightsync: Unsynchronized visual communication over screen-camera links," in *Proceedings of the 19th annual international conference on Mobile computing & networking*, 2013, pp. 15–26.
- [24] A. Wang, Z. Li, C. Peng, G. Shen, G. Fang, and B. Zeng, "Inframe++ achieve simultaneous screen-human viewing and hidden screen-camera communication," in *Proceedings of the 13th Annual International Conference on Mobile Systems, Applications, and Services*, 2015, pp. 181– 195.
- [25] S. Sastry, *Nonlinear systems: analysis, stability, and control*. Springer Science & Business Media, 2013, vol. 10.
- [26] J. Canny, "A computational approach to edge detection," *IEEE Transactions on pattern analysis and machine intelligence*, no. 6, pp. 679–698, 1986.
- [27] A. K. Das, R. Fierro, V. Kumar, J. P. Ostrowski, J. Spletzer, and C. J. Taylor, "A vision-based formation control framework," *IEEE transactions on robotics and automation*, vol. 18, no. 5, pp. 813–825, 2002.