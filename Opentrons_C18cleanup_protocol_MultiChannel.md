# **Automated C18 purification of extracted peptides for MS-metaproteomic analysis using Multi channel** 

Protocol created by: Paloma Lopez, Daniella Asturias, Mak Saito February 2026

# **Supplies:**

- Pierce C18 Tips, 100µl (Thermo Scientific, 87784)

- 4 NEST 12 Well Reservoir 15ml (Prod. no. nest-360102)

- 2 Kingfisher Shallow well plate (Prod. no. 97002540)

- 2 Kingfisher Deep well plate (Prod. no. 97002820)

- 1% trifluoroacetic acid (TFA)

- 50% acetonitrile (ACN)

- 0.1% TFA

- 0.1% TFA/5% ACN

- 0.1% Formic acid / 70% ACN

- Opentrons OT-2

> 

Notes: All solutions are made in LC/MS grade water (Optima W64). For instructions on stock reagents’ preparations click on the [<u>document link</u>](https://docs.google.com/spreadsheets/d/19EXv9J5pyjlpAfcDir9E9ICdOfBgafUizRDmBHi_MIA/edit?usp=sharing).

# **Protocol:**

1.  Turn instrument (switch on left back side) and computer on

2.  Select protocol XXXXXX and connect to Opentrons XXX

3.  Make sure all calibrations are Ready

    1.  In Labware Offset select “Run Labware Position Check”

    2.  Follow the instructions to calibrate the position of the labware

    3.  Need to confirm “Labware and Liquids” preferences

    4.  Scroll to the bottom of the page and select “Confirm preferences”

        1.  Only after confirming labware and liquids, the button to confirm preferences appears, only after confirming the preferences, the labware position offsets will be applied so make sure to do this!

4.  Once finished the Set up, wait until you have prepared all the plates before you start the run

5.  Prepare all tips needed in a single rack

    1.  Only add in the rack the number of tips needed for your samples

    2.  Check the filter in the tip as sometimes these do not cover the whole surface

6.  Transfer your samples to either a deep well plate or shallow plate

7.  Plates to prepare:

| **Solution** | **Type of plate** | **Volume to add** | **Place on deck** |
|----|----|----|----|
| 50% ACN | NEST 12 Well Reservoir | Add 250 uL per tip needed | 7 |
| 0.1% TFA | NEST 12 Well Reservoir | Add 250 uL per tip needed | 4 |
| 2% DMSO, 0.1% TFA | KF Deep well plate or shallow plate | Transfer 100 uL of sample | 1 |
| 0.1% TFA, 5% ACN | KF deep well plate | 230 uL per tip needed | 2 |
| 0.1% formic acid, 70% ACN | KF deep well plate | 100 uL per tip needed in columns 1-6. 130 uL in columns 7-12 if these are also needed (evaporation) | 3 |
| Waste plate for the 50% ACN | NEST 12 Well Reservoir | Empty | 8 |
| Waste plate for the 0.1% TFA | NEST 12 Well Reservoir | Empty | 5 |
| Waste for the 0.1% TFA, 5% ACN | KF deep well plate | Empty | 11 |

8.  When all the plates are ready, place them all in their correct location in the deck, as shown in the picture below:

<img width="807" height="280" alt="image1" src="https://github.com/user-attachments/assets/a69c4546-94f5-4154-a512-21648aa3b0e5" />


9.  Once all the plates have been placed you can start the run

10. Watch the first full run to make sure all the plates align and there are no crashes in the run

    1.  If the pipettor crashes with the plates cancel the run and do a Labware Check again

11. When all your samples have been run, you can cancel the program, unless you are using all 96 well in the plate

    1.  [<u>The program will follow the steps described in the section below</u>](#procedure-for-opentrons-ot-2-to-follow)

12. The samples will then be eluted in 0.1% formic acid, 70%acetonitrile solution

13. Transfer them to ethanol-cleaned 1.5 mL cryovials

14. Dry the samples in the speedvac at medium/low heat until dry

15. Resuspend peptides in 2% acetonitrile, 0.1% formic acid buffer

## **Procedure for Opentrons OT-2 to Follow:**

1\. Samples need to be previously acidified to a target concentration of 0.1% TFA to bring the pH down to ~4.

2\. C18 tips get conditioned by pipetting 100µl of 50% ACN. Volume is discarded into waste.

3\. 50% ACN rinse is repeated.

4\. Tips are equilibrated by aspiring 100µl of 0.1% TFA. Volume is discarded into waste.

5\. 0.1% TFA rinse is repeated.

6\. 100µl of sample is aspired and dispensed into the C18 tip slowly 5 times.

7\. Tip is rinsed by aspiring 100µl of 0.1% TFA/5% ACN. Volume is discarded into waste.

8\. 0.1% TFA/5% ACN rinse is repeated.

9\. Solution is eluted from the C18 matrix by aspiring and dispensing 5 times 100µl of 0.1% Formic Acid/70% ACN into a plate.

10\. Samples can be further processed for MS injection after C18 purification.

## **To Edit Protocol:**

1.  In Opentrons app, select “Protocol” and scroll to bottom of page

2.  Select “Protocol Designer,” which will open in a new browser\*

3.  “Import” protocol from device

4.  When done with edits, “Export” protocol to device

\*Computer must be connected to internet to Edit

**\*\*\*HIGHLY RECOMMENDED\*\*\***

- **Conduct labware position check before each run**

- **Perform test run (using Vitamin B12 solution helps visualize )**

**References:**

Thermo Scientific. *Pierce<sup>Ⓡ</sup> C18 Tips: Instructions version 2237.1.* Retrieved from [<u>https://www.thermofisher.com/document-connect/document-connect.html?url=https://assets.thermofisher.com/TFS-Assets%2FLSG%2Fmanuals%2FMAN0011713_Pierce_C18_Tip_UG.pdf</u>](https://www.thermofisher.com/document-connect/document-connect.html?url=https://assets.thermofisher.com/TFS-Assets%2FLSG%2Fmanuals%2FMAN0011713_Pierce_C18_Tip_UG.pdf)
