# DataProvision_LVGridResilience
This is a supplement to the Paper "Low Voltage Grid Resilience: Evaluating Electric Vehicle Charging Strategies in the Context of the Grid Development Plan Germany"

## Driving Profiles

The driving profiles are generated with the open source tool [SimBEV](https://github.com/rl-institut/simbev). SimBEV uses the database of the regularly updated study “Mobility in  Germany”, the biggest survey about daily mobility behaviourin Germany. The driving profiles include driving and idle events and are provided in the folder 'driving_profiles'. Each driving event includes information about the used energy, each standing event includes the location and the maximum power of the possible charging point. For the paper driving profiles of one week for every season were generated, since energy consumption of the BEVs differs between seasons. The assumption is made, that the BEVs charge exclusively at home.

## Charging Profiles

This study uses [SpiceEV](https://github.com/rl-institut/spice_ev) to apply four different charging strategies on the generated driving profiles. SpiceEV uses the energy demand and possible charging power of the given driving profiles to generate standing events, each with a specific ∆ SOC and a maximum charging power. The initial SOC is given by the SimBEV driving profiles. The resulting charging profiles are provided in the folder 'charging_profiles'.

## Electrical Profiles
The electrical profiles comprise household loads, heat pumps, electric vehicles and PV systems as input data for the [EnergyCellLV-Model](https://github.com/ricrei/energycell_lv_level). They are provided in the folder 'electrical_profiles' and were separated into seasonal periods. All profiles are compressed into a pickle file. To decompress them, use the script `decompress_inputfiles.py`.
These profiles can be applied to different low-voltage grids by conducting power flow calculations to evaluate the grid stress. In this study, the Simbench grids were examined.
