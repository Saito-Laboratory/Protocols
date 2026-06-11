# High-Throughput Proteomics Sample Preparation Using Magnetic Beads on the KingFisher System

**Created by:** Paloma Lopez and Dawn Moran

**Modified:** Paloma Lopez, Annie Stefanides, Rob Lampe (2025–2026)

---

## Introduction

This protocol describes a magnetic bead-based workflow for protein extraction, clean-up, and digestion from seawater and cultured biomass for mass spectrometry-based proteomics. The method integrates SP3 chemistry with automated processing using the KingFisher Flex system to improve throughput and reproducibility. This protocol yields purified and tryptic digested peptides ready for downstream LC-MS/MS analysis. This workflow has been optimised for seawater-derived samples and adapted for automated handling to increase consistency across large sample sets.

---

## Equipment and Supplies

- Eppendorf Centrifuge (Minispin Plus or 5810 R)
- Savant DNA120 SpeedVac Concentrator
- Eppendorf Thermomixer R
- 2.0 mL low-adhesion polypropylene microcentrifuge tubes with cap, ethanol-washed (cat. 1420-2600)
- 96-well deep-well tray
- Silicone cover for 96-well deep-well plate

**Additional supplies for filtered environmental samples:**

- Luer-slip 5 mL plastic syringe (S7510-5)
- 5 µm low protein-binding syringe filter, Millex-SV (SLSV025LS)
- 15 mL conical tube
- Vivaspin 6, 5,000 MWCO PES membrane (VS0611)

---

## Reagents

- Water, Optima LC/MS Grade (W6)
- Lysis buffer: 50 mM HEPES pH 8.5 (Boston BioProducts #BB-2082) / 2% SDS
- Benzonase Nuclease (Novagen 70746-3)
- 200 mM DTT in 50 mM HEPES pH 8.5
- 400 mM iodoacetamide in 50 mM HEPES pH 8.5
- Magnetic beads at 20 µg/µL in LCMS water
- 100% ethanol, HPLC/spectrophotometric grade, 200 proof (Sigma-Aldrich #459828)
- 100% acetonitrile
- 80% ethanol
- 50 mM HEPES pH 8.0 (Boston BioProducts #BB-2080)
- Trypsin in 50 mM HEPES pH 8.0 at 0.5 µg/µL
- 2% DMSO
- 1% formic acid (for cultured samples only)

> All solutions are prepared in LC/MS grade water (Optima W64).

---

## Procedure

### 1. Biomass Extraction

#### Environmental Marine Samples

1.1 Extract biomass from the filter using lysis buffer (2% SDS, 50 mM HEPES pH 8.5). If SDS has precipitated, pre-warm lysis buffer to 37 °C.
   - Using tweezers, unfold the filter and bend it to fully expose the biomass surface.
   - Submerge the filter in a 15 mL conical tube containing sufficient lysis buffer to fully cover it (~4 mL for one half of a 142 mm filter).
   - Heat at 95 °C for exactly 12 minutes. Do not exceed this time.
   - Incubate at room temperature for 30–60 minutes at 350 rpm.
   - Remove the filter, draining thoroughly before discarding.
   - Filter the lysate through a 5 µm syringe filter.
   - Rinse the syringe and filter with an additional 500 µL of lysis buffer.
   - Centrifuge at maximum speed (4,000 rpm for large rotor; 9,000 rpm for small rotor) for 20–30 minutes at room temperature.

1.2 Pre-rinse 5,000 MWCO Vivaspin tubes with ~900 µL of lysis buffer to remove contaminants. Centrifuge for ≥30 minutes, then discard residual buffer from both compartments.

1.3 Transfer the supernatant (excluding any pellet) to the rinsed Vivaspin tube and concentrate to ~400 µL.

1.4 Add 500 µL of lysis buffer to the concentrate and centrifuge again to ~400 µL.
   - If using a 5 mL Vivaspin: discard the flow-through from the lower chamber before adding buffer and re-centrifuging.

1.5 Transfer the concentrated sample to an ethanol-washed 2 mL cryovial, recording the final volume.
   - Final volume will depend on biomass content: 150–200 µL (low biomass) or 500–600 µL (high biomass). For optimal quantification accuracy, aim for a sample concentration that falls within the mid-range of the standard curve.

#### Cultured Samples

1.1 Transfer ~2 mL of culture (healthy density) to an ethanol-washed 2 mL low-adhesion microcentrifuge tube. Centrifuge at 14,100 × g for 20 minutes.
1.2 Remove and discard the supernatant. For low-yield samples, retain the supernatant as a backup.
1.3 Resuspend the pellet in 150–500 µL of lysis buffer (2% SDS, 50 mM HEPES pH 8.5) depending on biomass content. For optimal quantification accuracy, aim for a sample concentration that falls within the mid-range of the standard curve.
   -If the pellet does not fully resuspend, add additional buffer in 50 µL increments. Pre-warm lysis buffer to 37 °C if needed.
1.4 Heat at 95 °C for exactly 10 minutes. Do not exceed this time.
1.5 Incubate at room temperature for 30–60 minutes at 350 rpm.
1.6 Centrifuge at 14,000 rpm for 20–30 minutes at room temperature to pellet cell debris.
1.7 Transfer the supernatant to a new ethanol-washed tube. Retain the pellet only if targeting a specific protein.

> **Optional stopping point:** Samples may be stored at −20 °C. Thaw at room temperature or 37 °C before proceeding.

---

### 2. Protein Quantification

Quantify total protein in the lysate with preferred method.

---

### 3. Lysate Preparation

Aliquot **60 µg** of protein from the lysate. Add lysis buffer to bring the total volume to **300 µL** (final concentration: 0.2 µg/µL).

- Adjust reagent volumes proportionally if the initial sample volume differs.
- Archive the remaining lysate at −80 °C.

> **Optional stopping point:** Samples may be stored at −20 °C. Thaw at room temperature or 37 °C before proceeding.

---

### 4. Chromatin Degradation

Add **2 µL** (50 units) of benzonase nuclease. Incubate at 37 °C for 30–40 minutes. This step degrades chromatin, which would otherwise disrupt SP3 clean-up.

---

### 5. Reduction

Working in a fume hood, add **15 µL** of 200 mM DTT in 50 mM HEPES pH 8.5 (5 µL per 100 µL lysate). Incubate at 45 °C for 30 minutes. This step reduces disulfide bonds.

---

### 6. Alkylation

Working in a fume hood, add **30 µL** of 400 mM iodoacetamide in 50 mM HEPES pH 8.5 (10 µL per 100 µL lysate). Incubate in the dark at 24 °C for 30 minutes. This step alkylates free sulfhydryl groups.

---

### 7. Quenching

Add **30 µL** of 200 mM DTT in 50 mM HEPES pH 8.5 (10 µL per 100 µL lysate). Incubate at room temperature for ≥10 minutes to quench unreacted iodoacetamide.

> **Optional stopping point:** Samples may be stored at −20 °C. Thaw at room temperature or 37 °C before proceeding.

---

### 8. Protein Clean-up

> **Important:** Do not freeze samples once beads have been added.

8.1 Add **30 µL** of magnetic beads at 20 µg/µL (10:1 bead-to-protein ratio; 600 µg beads per 60 µg protein).

8.2 Immediately add **407 µL** of 100% ethanol to achieve a final 50% ethanol concentration, promoting protein binding to the beads.

8.3 Mix thoroughly by pipetting or vortexing, ensuring beads do not adhere to tube walls.

8.4 Incubate at room temperature for 15 minutes at 650 rpm. If needed, briefly centrifuge at ≤1,000 rpm for 2 seconds.

> **Note:** From this point forward, samples are transferred to 96-well deep-well trays. The KingFisher Flex replaces manual magnetic racks.

8.5 Transfer samples from microcentrifuge tubes to the 96-well deep-well tray using a multichannel pipette. Record tray positions in the lab notebook (positions labeled A–H, 1–12).

8.6 Prepare the following reagent trays, using a multichannel pipette:

| Tray | Reagent | Volume per well |
|------|---------|-----------------|
| Starting sample | Samples transferred from microcentrifuge tubes | 814 µL |
| Wash 1 (Ethanol_1) | 80% ethanol | 700 µL |
| Wash 2 (Ethanol_2) | 80% ethanol | 700 µL |
| Binding (Acetonitrile) | 100% acetonitrile | 700 µL |
| Elution | 100 mM ammonium bicarbonate or 50 mM HEPES pH 8.0 | 90 µL |

8.7 Connect the laptop to the KingFisher Flex and power on the instrument. Open BindIt 4.1 software and confirm the instrument is connected (status shown at the bottom of the window). The instrument screen should display "Computer control" when connected.

8.8 If not connected: select Connect → 711-85562 and confirm the instrument screen displays "Computer control."

8.9 In the Home tab, select **ProteinCleanUp_v2.bdz** from recent protocols (or open via the file browser). Select Start. When prompted, save the run report to: Desktop → BindIt 4.1 → Report Files.

8.10 Follow on-screen instructions to load trays in the correct orientation (A1 corner indicated). Press Start after loading each tray.

8.11 Monitor the run periodically.

8.12 When KingFisher program is over, quantify purified protein using the BSA assay.

8.13 Calculate trypsin volume for each sample at a 1:20 trypsin-to-protein ratio.

8.14 Add trypsin (0.5 µg/µL in 100 mM ammonium bicarbonate or 50 mM HEPES pH 8.0) to each well.

8.15 Cover the sample tray with a silicone lid and incubate overnight (14 hours) at 37 °C, 400 rpm.

> **Important:** Do not freeze samples containing beads at any point.

---

### 9. Peptide Recovery

9.1 Following overnight incubation at 37 °C, centrifuge the plate in the tray centrifuge adapter at 1,000 rpm for 20 seconds to collect condensation from the lid. Do not exceed this speed.

9.2 Remove beads by running **BeadRemoval.bdz** on the KingFisher Flex. Required materials:
    - New comb in a comb plate
    - Sample plate

9.3 Add **20 µL** of fresh bead solution (20 µg/µL) to each sample well. Shake the plate to fully resuspend the beads.

9.4 Add **1,790 µL** of 100% acetonitrile to each well (~94% final acetonitrile concentration). Mix thoroughly by pipetting, scraping the bottom and walls of each well to release beads.

9.5 Distribute the solution equally across two plates (950 µL per plate; maximum volume to avoid overflow when comb is submerged).

9.6 Cover the plates and incubate at room temperature for 20 minutes on the thermomixer at 450–550 rpm.

9.7 Prepare the following solutions for the next KingFisher Flex run:

| Tray | Reagent | Volume per well |
|------|---------|-----------------|
| Wash (Acetonitrile) | 100% acetonitrile (deep-well plate) | 700 µL |
| DMSO Elution | 2% DMSO (shallow-well plate) | 90 µL |

9.8 Load **PeptideRecovery_Round1_v3.bdz** in BindIt 4.1. Follow on-screen loading instructions. The protocol will combine both half-volume plates into a single output.

9.9 When prompted, save the run report to: Desktop → BindIt 4.1 → Report Files. Start the protocol.

9.10 Once complete, use a magnetic block to confirm that beads have been removed from solution. If beads are detected, transfer the eluate to a new plate and repeat magnetic separation.

9.11 Add **10 µL** of 1% TFA (first step of C18 clean-up protocol).

> **Optional stopping point:** Samples may be stored at −20 °C. Thaw before proceeding.

9.12 Proceed to the manual or automated C18 clean-up protocol.

9.13 Store samples at −20 °C for short-term MS analysis or at −80 °C for long-term storage.

---

## References

1. Hughes CS, Foehr S, Garfield DA, Furlong EEM, Steinmetz LM, Krijgsveld J. Ultrasensitive proteome analysis using paramagnetic bead technology. *Mol Syst Biol.* 2014;10(10):757. doi:10.15252/msb.20145625

2. Hughes CS, Moggridge S, Müller T, Sorensen PH, Morin GB, Krijgsveld J. Single-pot, solid-phase-enhanced sample preparation for proteomics experiments. *Nat Protoc.* 2019;14(1):68–85. doi:10.1038/s41596-018-0082-x

3. Cytiva Life Sciences. Cleanup for mass spectrometry using Sera-Mag SpeedBeads [Internet]. Cytiva; [cited 2025]. Available from: https://www.cytivalifesciences.com/en/us/insights/cleanup-for-mass-spectrometry
