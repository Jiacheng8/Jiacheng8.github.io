---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<section class="home-hero" id="about-me">
  <div class="home-hero__kicker">Machine Learning · MBZUAI</div>
  <h1 class="home-hero__title">Building efficient intelligence from <span>better data.</span></h1>
  <p class="home-hero__lead">I’m Jiacheng Cui (崔家诚), a PhD student exploring data-centric AI, dataset distillation, and efficient training. Previously, I graduated with First Class Honours in AI and Computer Science from the University of Edinburgh.</p>
  <div class="home-hero__actions">
    <a class="home-hero__button home-hero__button--primary" href="#publications">Explore my research</a>
    <a class="home-hero__button" href="mailto:jiachengcui5@gmail.com">Let’s collaborate</a>
  </div>
  <div class="home-hero__topics" aria-label="Research interests">
    <span>Data-centric AI</span>
    <span>Dataset distillation</span>
    <span>Efficient training</span>
  </div>
</section>

# News {#news}
- *2026.08*: &nbsp;🎉🎉 *PIXAR* has been accepted to **ECCV 2026**. See you in Malmö!
- *2026.04*: &nbsp;🎉🎉 *HALD* has been accepted to **ICML 2026**. See you in Seoul!
- *2026.04*: &nbsp;🎉🎉 *LLMSurgeon* has been accepted to **ACL 2026**. See you in San Diego!
- *2025.09*: &nbsp;🎉🎉 *FADRM* has been accepted to **NeurIPS 2025**. See you in San Diego!


# Selected Publications {#publications}

<div class='publication-scroll' markdown="1">

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ECCV 2026</div><img src='images/PIXAR.png' alt="PIXAR overview" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[From Masks to Pixels and Meaning: A New Taxonomy, Benchmark, and Metrics for VLM Image Tampering](https://arxiv.org/abs/2603.20193)

Xinyi Shang<sup>*</sup>, Yi Tang<sup>*</sup>, **Jiacheng Cui**<sup>*</sup>, Ahmed Elhagry, Salwa K. Al Khatib, Sondos Mahmoud Bsharat, Jiacheng Liu, Xiaohan Zhao, Jing-Hao Xue, Hao Li, Salman Khan, Zhiqiang Shen

[**Project**](https://github.com/VILA-Lab/PIXAR) <strong><span class='show_paper_citations' data=''></span></strong>
- VLM Image Tampering Benchmarking
- Pixel-level Detection
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ACL 2026</div><img src='images/LLM-surgeon.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[LLMSurgeon: Diagnosing Data Mixture of Large Language Models]()

Yaxin Luo<sup>*</sup>, **Jiacheng Cui**<sup>*</sup>, Xiaohan Zhao, Xinyi Shang, Jiacheng Liu, Xinyue Bi, Zhaoyi Li, Zhiqiang Shen

[**Project**]() <strong><span class='show_paper_citations' data=''></span></strong>
- Data Mixture Surgery
- Label Shift Inversion
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICML 2026</div><img src='images/HALD.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Hard Labels In! Rethinking the Role of Hard Labels in Mitigating Local Semantic Drift](https://arxiv.org/pdf/2512.15647)

**Jiacheng Cui**, Bingkui Tong, Xinyue Bi, Xiaohan Zhao, Jiacheng Liu, Zhiqiang Shen

[**Project**](https://github.com/Jiacheng8/HALD) <strong><span class='show_paper_citations' data='SI_9kD0AAAAJ:hqOjcs7Dif8C'></span></strong>
- Dataset Distillation
- Label Usage
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Neurips 2025</div><img src='images/FADRM.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[FADRM: Fast and Accurate Data Residual Matching for Dataset Distillation](https://arxiv.org/pdf/2506.24125)

**Jiacheng Cui**<sup>*</sup>, Xinyue Bi<sup>*</sup>, Yaxin Luo, Xiaohan Zhao, Jiacheng Liu, Zhiqiang Shen

[**Project**](https://github.com/Jiacheng8/FADRM) <strong><span class='show_paper_citations' data='SI_9kD0AAAAJ:W7OEmFMy1HYC'></span></strong>
- Dataset Distillation
- Data Residual Matching
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Preprint</div><img src='images/CV-DD.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Dataset Distillation via Committee Voting](https://arxiv.org/pdf/2501.07575?)

**Jiacheng Cui**, Zhaoyi Li, Xiaochen Ma, Xinyue Bi, Yaxin Luo, Zhiqiang Shen

[**Project**](https://github.com/Jiacheng8/CV-DD) <strong><span class='show_paper_citations' data='SI_9kD0AAAAJ:u-x6o8ySG0sC'></span></strong>
- Dataset Distillation
- Committee Voting
</div>
</div>

- <span class="conf-tag">ICML 2026</span> [Next-Gen CAPTCHAs: Leveraging the Cognitive Gap for Scalable and Diverse GUI-Agent Defense](https://arxiv.org/pdf/2602.09012), Jiacheng Liu*, Yaxin Luo*, **Jiacheng Cui**, Xinyi Shang, Xiaohan Zhao, Zhiqiang Shen. [![](https://img.shields.io/github/stars/Greenoso/BiGain?style=social&label=Code+Stars)](https://github.com/MetaAgentX/NextGen-CAPTCHAs)

- <span class="conf-tag">CVPR 2026</span> [BiGain: Unified Token Compression for Joint Generation and Classification](https://arxiv.org/pdf/2603.12240), Jiacheng Liu, Shengkun Tang, **Jiacheng Cui**, Zhiqiang Shen. [![](https://img.shields.io/github/stars/Greenoso/BiGain?style=social&label=Code+Stars)](https://github.com/Greenoso/BiGain)


- <span class="conf-tag">NeurIPS 2025</span> [Open CaptchaWorld: A Comprehensive Web-based Platform for Testing and Benchmarking Multimodal LLM Agents](https://arxiv.org/abs/2505.24878), Yaxin Luo, Zhaoyi Li, Jiacheng Liu, **Jiacheng Cui**, Xiaohan Zhao, Zhiqiang Shen. [![](https://img.shields.io/github/stars/MetaAgentX/OpenCaptchaWorld?style=social&label=Code+Stars)](https://github.com/MetaAgentX/OpenCaptchaWorld)

- <span class="conf-tag">NeurIPS 2025</span> [A Frustratingly Simple Yet Highly Effective Attack Baseline: Over 90% Success Rate Against the Strong Black-box Models of GPT-4.5/4o/o1](https://arxiv.org/abs/2503.10635), Zhaoyi Li, Xiaohan Zhao, Dong-Dong Wu, **Jiacheng Cui**, Zhiqiang Shen. [![](https://img.shields.io/github/stars/VILA-Lab/M-Attack?style=social&label=Code+Stars)](https://github.com/VILA-Lab/M-Attack)


</div>

# Honors and Awards {#honors}
- **2024–2026**, MBZUAI Graduate Fellowship (Full Scholarship)
- **2024. 06**, Awarded First-Class Honours upon Graduation, University of Edinburgh

# Education {#education}
- **2026.08 – 2030.06 (expected)**, Doctor of Philosophy (Ph.D.) in Machine Learning, MBZUAI, Abu Dhabi, UAE
- **2024.09 – 2026.06**, Master of Science (M.Sc.) in Machine Learning, MBZUAI, Abu Dhabi, UAE
- **2019.09 – 2024.06**, Bachelor of Science (B.Sc.) in Artificial Intelligence and Computer Science, The University of Edinburgh, UK


# Academic Service {#service}

## Reviewer
- <span style="color:#1f77b4;">2026</span>: ICLR, TMLR, NeurIPS



# Experience {#experience}
- *2022.05 - 2022.07*, [Intersim (英特仿真)](http://www.intesim.cn/), Dalian, China.
