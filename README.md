# PeriodicSimAPI
This is the API for my [PeriodicSim project](https://thekonamicode.itch.io/periodicsim) that has all the elements and compounds and mixtures in it.
The API is in JSON format and the various different substances are shown in different ways.

**FOR ELEMENTS**
```json
{ 
  "name": "hydrogen", 
  "atomicNum": 1, 
  "chemicalFormula": "H", 
  "type": "nonmetal", 
  "info": "Hydrogen is an unstable element with 1 proton and electron. It is the most abundant element with around 90% of atoms being hydrogen." 
}
```
**FOR COMPOUNDS AND MOLECULES (THEY ARE THE SAME)**
```json
{
  "name": "water", 
  "chemicalFormula": "H2O", 
  "colour": "Green", 
  "info": "Water is vital for life - without it, we simply can't exist. It is neither acid nor alkali, with a pH level of 7.", 
  "components": [ ["hydrogen", 1], ["hydrogen", 1], ["oxygen", 2] ], 
  "connections": [ 
    { "connector": "oxygen", "connected": "hydrogen", "bond": "convalent" }, 
    { "connector": "oxygen", "connected": "hydrogen", "bond": "convalent" } 
  ] 
}
```
The components are the components and how many other elements they are connectied to.
The connections are the various different connections which can be seen in the compound. In water, an oxygen is connected to hydrogen and an oxygen is connected to water again.

**FOR MIXTURES**
```json
{ 
  "name": "hydrochloric acid", 
  "chemicalFormula": "HCl+H2O", 
  "colour": "Red", 
  "info": "Hydrochloric acid is an important chemical reagent and industrial chemical, used in the production of polyvinyl chloride for plastic." 
}
```

**FOR REACTIONS**
```json
{ 
  "reactants": [ "hydrogen chloride", "water" ], 
  "products": [ "hydrochloric acid" ] 
}
```
