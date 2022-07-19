# DARSH: Deceiving Adversaries through Redirection

## Intro
This repository contains the contents and configurations of the work done in the paper entitled "DARSH: Deceiving Adversaries through Redirection to
Semi-Indistinguishable Honeypot Web Servers".

DARSH is emulated within the [Common Open Research Emulator (CORE)](https://github.com/coreemu/core) and utilizes the work of [Cyber Deception Experimentation System (CDES)](https://github.com/ARL-UTEP-OC/cdes) to redirect attacker to one or more than one semi-indistinguishable honeypots.

In this artifact, we only present the [testbed file](CORE%20Sample%20File/DARSH_final.imn) and associated configurations. We used the base of CDES that presents the underlying logics of the [Monitor](https://github.com/ARL-UTEP-OC/cdes/tree/master/Monitor), [Swapper](https://github.com/ARL-UTEP-OC/cdes/tree/master/Swapper), and [Trigger](https://github.com/ARL-UTEP-OC/cdes/tree/master/Trigger). We also used the same [Hooks](https://github.com/ARL-UTEP-OC/cdes/tree/master/sample/hooks) used in CDES.

## Video Illustration (GIF)

Below, there is a sample screenshot of the working demo. Here, we show that how attacker is being redirected to a semi-indistinguishable honeypot after sending certain number of ping packets to the target IP address. The attacker node is a Kali Linux machine. Note that, the blue line denotes an active connection where the yellow lines denote inactive connection. Ping does not get interrupted as the semi-indistinguishable honeypot has the same IP address. 

![VideoIllustration](./screenshot/short_demo.gif)