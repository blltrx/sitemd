---
path: projects/nano.html
---
# NanoQuEST

last updated: 2025-07-14

between 2021 and 2023 i lead a research group as part of a school extracurricular project. NanoQuEST aimed to electrospin nanofibres. this pages aims at documenting a large chunk of the project. this page is primarily about the progress made while i was involved.


## background

![example of a nanofibre, with a minimum diameter of 797nm](/assets/IMAGE-SEM-nanofiber.webp) [download](https://files.roseis.gay/nano/SEM-nanofiber.webp)  
![](/assets/setupdiagram.webp) [download](https://files.roseis.gay/nano/IMAGE-setupdiagram.webp)

we used two materials to create out nanofibres, alpha-cellulose and polyethylene oxide. We focused on the cellulose fibres as they tend to spin better.

to make the solution to spin cellulose fibres, we mixed together alpha-cellulose, and ionic liquid, and dimethyl sulfoxide (DMSO) to force it to dissolve together.

we used two ionic liquids, 1-ethyl-3-methylimidazolium diethyl phosphate (phosphate) and 1-ethyl-3-methylimidazolium acetate (acetate). we found the acetate solutions were more reliable.

we recorded our solutions based on the ratio of DMSO to ionic liquid, and the percentage by mass of cellulose (calculated by mass of (DMSO + ionic liquid) x (target percentage / 100)). our most successful and reliable solution was 1:1 acetate 2.5% cellulose.

for the polyethylene oxide (PEO) solutions we initially used PEO with a molecular weight of 4M mixed with distilled water. we found around 2.5% PEO by mass worked best, again percentage calculated similarly to above.

we can spin the solutions by placing them in a syringe, and applying a high potential between the needle and a conductive collection plate while slowly pushing the solution out of the syringe with a syringe pump. we generally used an acceleration voltage of 5kV, a distance of <5cm, and an extrusion rate of 0.25ml/h to 0.5ml/h.

![a needle full of a cellulose based electrospinning solution](/assets/IMAGE-a-solution.webp) [download](https://files.roseis.gay/nano/IMAGE-a-solution.jpg)

<!-- our method sheet is [available for download](https://files.roseis.gay/nano/main.pdf) via files.roseis.gay -->

---

## ageing

we observed in 2021 that the age of our cellulose solutions may affect its ability to spin. we decided to investigate further

we created a range of solutions, and spun them once a week over a period of 6 weeks.

![results table showing that across four solutions, the most success is found between 2-3 weeks](/assets/CHART-initial-ageing.webp) [download](https://files.roseis.gay/nano/CHART-initial-ageing.png)

our results matched our initial observations, and suggested that the phosphate solutions are optimal at around 2 to 3 weeks. we didn’t have enough data to draw conclusions of the acetate solutions.

we spoke with Dr Marcus Johns about why this could be happening, and we came up with the hypothesis that, with cellulose being hydrophilic, the solutions were drawing moisture from the water vapour in the air.

we devised an experiment to test this

all spinnable solutions within the ageing experiments are cellulose solutions, within M1 the only ionic liquid used was 1-ethyl-3-methylimidazolium diethyl phosphate, as we do not currently have any 1-ethyl-3-methylimidazolium acetate (which generally spins more reliably).

all ratios refer to dimethyl sulfoxide : ionic liquid in that order without exception.

if our hypothesis is correct, we expect to see some overall mass gain, as the cellulose is hydrophilic and will absorb water vapour when humidity is high.

### method 1 (M1)

electrospin a series of solutions as close to daily as possible, recording mass difference *between* the spins when idle.

The solutions spun where as follows:  

- 1:1 dimethyl sulfoxide to 1-ethyl-3-methylimidazolium diethyl phosphate 2.5% cellulose  
- 1:1 dimethyl sulfoxide to 1-ethyl-3-methylimidazolium diethyl phosphate 2.5% cellulose  
- 1:1 dimethyl sulfoxide to 1-ethyl-3-methylimidazolium diethyl phosphate 3.75% cellulose  
- 3:1 dimethyl sulfoxide to 1-ethyl-3-methylimidazolium diethyl phosphate 2.5% cellulose

the solutions were stored in the NanoQuEST cupboard in the corner of the lab, and as such were in an environment with variable humidity and temperature.

### results

![graph of cumulative mass difference over time showing an unreliable trend upwards](/assets/CHART-M1.svg) [download](https://files.roseis.gay/nano/CHART-M1.svg)

the graph above shows the cumulative mass gain/loss over time, that is, the sum of mass differences between spins, separated into distinct series for each solution. The #00D etc. refers to an internal stock ID number.

our two 1:1 2.5% phosphate solutions were manufactured at the same time, and spun in parallel. there is a fluctuation between 10/11/23 and 13/11/23 that seems to self correct. This could be systematic error, as the two solutions behave in parallel.

a single 1:1 2.5% phosphate solution (#00E pictured in blue) suddenly gains 0.51g between 16/11/23 and 17/11/23, while no other solution does. It later loses a similar amount of mass, 'self correcting', between 29/11/23 and 30/11/23.

the 1:1 3.75% phosphate and 3:1 2.5% phosphate solutions behave in parallel quite reliable, and slowly gain mass, with a major anomaly between 13/12/23 and 314/12/23 where they suddenly loosing a lot of mass. as they act in parallel with each other, it is lightly this is systematic error.

overall all solutions seem to gain some mass, but with a lot of chaos.

the average mass change is +0.6g per 1.7 days.

our mass uncertainty for individual measurements is +/- 0.2g, however there are factors that could raise this between measurements.  

- we changed the mass scale we were using to measure midway though the experiment  
- there might have been moisture or debris on the syringe / needle cap  
- the scale may not have been tared to be set to zero before a measurement on any given day

the humidity and temperature the solutions were stored in was not tracked, and during the experiment there were some days with vegrary high CO2 content and pollutants in the air that may have affected the humidity abnormally. (this was due to some soil burning in an adjacent lab).

the individual mass change measurements were often within the uncertainty range, makes it practically impossible to draw any significant conclusions from this data.

no solutions successfully formed nanofibers throughout the whole trial, which suggests significant issues with the solutions.

### conclusions

we cannot draw any firm conclusions from this data, due to the significant uncertainty in the data.  
however, ignoring outliers, there is a slight upwards trend in the cumulative mass difference. This does suggest that there is some change. We decided to investigate this further with a revised method.  

### method 2 (M2)

we are looking at how the age of solutions affects spin. M2 is testing if water gain could be responsible for the difference in ageing effects by storing solutions in a low humidity environment, and variable humidity environment.

all spinnable solutions within the ageing experiments are cellulose solutions, within M2 the only ionic liquid used was 1-ethyl-3-methylimidazolium diethyl phosphate, as we do not currently have any 1-ethyl-3-methylimidazolium acetate (which generally spins more reliably).

M2 also stores some non cellulose solutions as a control.

all ratios refer to dimethyl sulfoxide : ionic liquid in that order without exception.

if our hypothesis is correct, we expect to see some overall mass gain, as the cellulose is hydrophilic and will absorb water vapour when humidity is high.

our method was to manufacture several different solutions, and split each one into two roughly equal beakers. store one half in a tray in open air, and the other half in a desiccator.

the solutions used are as follows:  

- 1:1 dimethyl sulfoxide to 1-ethyl-3-methylimidazolium diethyl phosphate 2.5% cellulose  
- 1:1 dimethyl sulfoxide to 1-ethyl-3-methylimidazolium diethyl phosphate 2.5% cellulose  
- 1:1 dimethyl sulfoxide to 1-ethyl-3-methylimidazolium diethyl phosphate 1.25% cellulose  
- 1:1 dimethyl sulfoxide to 1-ethyl-3-methylimidazolium diethyl phosphate 5% cellulose  
- dimethyl sulfoxide  
- 3% Polyethylene Oxide in distilled water

the humidity of the open air (wet) solutions were recorded by a data logger half hourly.

![graph of cumulative mass difference over time showing an unreliable trend upwards](/assets/CHART-M2.svg) [download](https://files.roseis.gay/nano/CHART-M2.svg)

our results show a significant mass gain in all cellulose solutions stored in open air (wet) conditions. the solutions stored in a low humidity environment, i.e. in the desiccator, gained significantly less mass by at least a factor of a half. the solution that was only DMSO gained the most mass. the average conditions of the wet solutions were 54% humidity at 15.9 C. the solutions were between 08/02/23 to 21/02/23 inclusive.  

our mass uncertainty per measurement was +/- 0.01g. our mass gains are significantly higher than our uncertainties. our results suggest that the solutions do in fact gain water vapour and this affects the solutions over time. the increase in mass outside the desiccator in the DMSO sample suggests that this gain is from the DMSO taking up water vapour, not the cellulose. this would make sense as there is far more DMSO than cellulose in any solution. increased water content will affect the conductivity and viscosity of solutions. we also observed that it caused the wet solutions to separate. this would happen much more slowly usually, as when they are stored in the needle they are in contact with the air far less. overall M2 has been far more reliable than M1 in results, and clearly indicates that the solutions do take up water vapour from the air.

---

## storage experimentation

based on the research done on ageing, finding a storage method for our solutions that would reduce water vapour uptake as much as reasonably possible became a priority. we placed 25 ml of pure DMSO in an open air environment, in a desiccator, and in a freezer and recorded the mass incrementally.  
![graph of cumulative mass difference over time showing an unreliable trend upwards](/assets/CHART-ageing-storage.svg) [download](https://files.roseis.gay/nano/CHART-ageing-storage.svg)

from the graph above it's clear that while the desiccator has the minimal amount of mass gain, storing solutions in a freezer has a similar rate of mass gain and is 1/10th of the rate of gain than an exposed lab environment such as a cupboard. this makes a freezer a very easy and effective storage method going forwards.

---

## rotating drum

we tried to build a rotating drum to act as a collector plate. our prototype, a aluminium can with a motor attached, did work but had too much friction to spin consistently.  
we are currently building an improved one

![prototype rotating drum, made from an aluminium drinks can](/assets/IMAGE-drum-and-arduino.webp) [download](https://files.roseis.gay/nano/IMAGE-drum-and-arduino.jpg)  
the rotating drum allows us to align our fibres on collection, but also stretch them slightly to further reduce to diameter.

---

## polyethylene oxide

we worked with students at North Penn High School, Pennsylvania, USA to experiment with spinning polyethylene oxide fibres  
this is in progress currently, we are currently perameter testing 4M PEO  

---

## research presentation

we have attended the 2022/3 science conferences at Tonbridge School and presented our research on electrospinning nanofibres as a research poster  
we also attended the 2022/3 IRIS London conferences and presented our research as both a poster, and a talk to 400 people.  

![research poster for the 2022 conferences. Contains a summary of the infomating in the method document](/assets/poster-2022.webp) [download](https://files.roseis.gay/nano/poster-2022.pdf)

  
a lot of time (arguably too much) was dedicated to our b r a n d i n g. we made a logo, a theme colour, and a whole lot of posters and documents.  

for resources and files, email me! full names of students have been redacted.

and that's NanoQuEST! its one of my favorite things i’ve been able to do so far. doing actual lab work that i have to design and manage myself for my own hypotheses is really fun, and i also got to do it with really nice people, which is also very cool.

if you have any questions, i would love to answer them! the most reliable way to contact me is by emailing [hello@roseis.gay](mailto:hello@roseis.gay).
