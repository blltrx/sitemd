---
path: /projects/plat0-scraper.html
---

# historical platform allocation scraper 🦀

as part of my mission to [visit every platform zero](/projects/plat0), i needed to know what the calling pattern at Stockport station was at its platform zero. unfortunatly it seemed very irregular as to which booked services actually called at the platform. as such, i made this scraper for [RealTimeTrains](https://realtimetrains.co.uk) that looks at actual historial platform allocation for all services at any UK railway station for any time period that RealTimeTrains holds such data. where a platform cannot be determined (either because it's a bus replacement service, or the train hasn't yet called at the station) it is set as 255.

it outputs a csv style output to stdout, and can be found [on my github](https://github.com/blltrx/plat0). it can be installed using 'cargo install --git'.
