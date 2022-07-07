# DARSH: Deceiving Adversaries through Redirection

This repository contains the contents and configurations of the work done in the paper entitled "DARSH: Deceiving Adversaries through Redirection to
Semi-Indistinguishable Honeypot Web Servers".

DARSH is emulated within the [Common Open Research Emulator (CORE)](https://github.com/coreemu/core) and utilizes the work of [Cyber Deception Experimentation System (CDES)](https://github.com/ARL-UTEP-OC/cdes) to redirect attacker to one or more than one semi-indistinguishable honeypots.

In this artifact, we only present the [testbed file](CORE%20Sample%20File/DARSH_final.imn) and associated configurations. We used the base of CDES that presents the underlying logics of the [Monitor](https://github.com/ARL-UTEP-OC/cdes/tree/master/Monitor), [Swapper](https://github.com/ARL-UTEP-OC/cdes/tree/master/Swapper), and [Trigger](https://github.com/ARL-UTEP-OC/cdes/tree/master/Trigger). We also used the same [Hooks](https://github.com/ARL-UTEP-OC/cdes/tree/master/sample/hooks) used in CDES.
