from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

elements = [
	{
      "name": "hydrogen",
      "atomicNum": 1,
      "chemicalFormula": "H",
      "type": "nonmetal",
      "info": "Hydrogen is an unstable element with 1 proton and electron. It is the most abundant element with around 90% of atoms being hydrogen."
    },
    {
      "name": "helium",
      "atomicNum": 2,
      "chemicalFormula": "He",
      "type": "noble gas",
      "info": "Helium is a noble gas, meaning that it is perfectly stable by itself. This means that it does not react with many things."
    },
    {
      "name": "lithium",
      "atomicNum": 3,
      "chemicalFormula": "Li",
      "type": "alkali metal",
      "info": "Lithium is the densest, yet lightest metal. It is also one of the oldest elements."
    },
    {
      "name": "berylium",
      "atomicNum": 4,
      "chemicalFormula": "Be",
      "type": "alkaline earth",
      "info": "Berylium is non-magnetic with 2 valence electrons. It is the 44th most abundant metal in the earth's crust."
    },
    {
      "name": "boron",
      "atomicNum": 5,
      "chemicalFormula": "B",
      "type": "semimetal",
      "info": "Boron is a very important part of the nuclear industry. It is used to make nuclear rods."
    },
    {
      "name": "carbon",
      "atomicNum": 6,
      "chemicalFormula": "C",
      "type": "nonmetal",
      "info": "Carbon is the basis for organic chemistry; it occours in all living things. Even the simplest organic molecules consist of carbon bonded to hydrogen."
    },
    {
      "name": "nitrogen",
      "atomicNum": 7,
      "chemicalFormula": "N",
      "type": "nonmetal",
      "info": "Nitrogen makes up most of the earth's atmosphere - around 78.05%. It is also the 6th most abundant element in the universe."
    },
    {
      "name": "oxygen",
      "atomicNum": 8,
      "chemicalFormula": "O",
      "type": "nonmetal",
      "info": "Oxygen. The gas that we all breathe. It gives life to every creature on earth - 2/3 of the human body is made out of oxygen."
    },
    {
      "name": "florine",
      "atomicNum": 9,
      "chemicalFormula": "F",
      "type": "halogen",
      "info": "Fluorine is the most reactive and electromagnetive of all the chemical elements. The only gasses it does not reactive are oxygen, helium, neon and argon."
    },
    {
      "name": "neon",
      "atomicNum": 10,
      "chemicalFormula": "Ne",
      "type": "noble gas",
      "info": "Neon is one of the only gasses that do not react with fluorine. It's prmary use is to make neon signs for advertising."
    },
    {
      "name": "sodium",
      "atomicNum": 11,
      "chemicalFormula": "Na",
      "type": "alkali metal",
      "info": "Sodium is a highly reactive silvery-white metal that needs to be kept in oil as it spontaneously combusts with water."
    },
    {
      "name": "magnesium",
      "atomicNum": 12,
      "chemicalFormula": "Mg",
      "type": "alkaline earth",
      "info": "Magnesium is essential for animal and plant nutrition and is found in a variety of foods we eat and many everyday products."
    },
    {
      "name": "alumnium",
      "atomicNum": 13,
      "chemicalFormula": "Al",
      "type": "basic metal",
      "info": "Alumnium is present in more than 270 minerals, making it the most abundant mineral on Earth after Oxygen and Silicon."
    },
    {
      "name": "silicon",
      "atomicNum": 14,
      "chemicalFormula": "Si",
      "type": "semimetal",
      "info": "Silicon is the seventh most abundant chemical element in the universe and second most abundant on the planet after oxygen."
    },
    {
      "name": "phosphorus",
      "atomicNum": 15,
      "chemicalFormula": "P",
      "type": "nonmetal",
      "info": "Phosphorous is an essential mineral that can be found in bones, DNA and RNA."
    },
    {
      "name": "sulfur",
      "atomicNum": 16,
      "chemicalFormula": "S",
      "type": "nonmetal",
      "info": "Sulfur is an element found in amino acids and protein, making it essential to life."
    },
    {
      "name": "chlorine",
      "atomicNum": 17,
      "chemicalFormula": "Cl",
      "type": "halogen",
      "info": "Chlorine is the second-lightest element in the periodic table after fluorine. Like other halogens, it is highly reactive and is found in a lot of compounds."
    },
    {
      "name": "argon",
      "atomicNum": 18,
      "chemicalFormula": "Ar",
      "type": "noble gas",
      "info": "Argon comes form the Greek word for lazy, and for over a 100 years after its discovery, chemists were unable to get it to react with anything until 2000"
    },
    {
      "name": "potassium",
      "atomicNum": 19,
      "chemicalFormula": "K",
      "type": "alkali metal",
      "info": "Potassium is the seventh most abundant chemical on our planet. It was also the first elemenal metal to be found through electrolysis."
    },
    {
      "name": "calcium",
      "atomicNum": 20,
      "chemicalFormula": "Ca",
      "type": "alkaline earth",
      "info": "Calcium is found in many foods and is also in your bones and teeth."
    }
	]

compounds = [
    	{
			"name": "water",
			"chemicalFormula": "H2O",
			"colour": "Green",
			"info": "Water is vital for life - without it, we simply can't exist. It is neither acid nor alkali, with a pH level of 7.",
			"components": [
				["hydrogen", 1],
				["hydrogen", 1],
				["oxygen", 2]
			],
			"connections": [
				{
					"connector": "oxygen",
					"connected": "hydrogen",
					"bond": "convalent"
				},
				{
					"connector": "oxygen",
					"connected": "hydrogen",
					"bond": "convalent"
				}
			]
		},
		{
			"name": "carbon dioxide",
			"chemicalFormula": "CO2",
			"colour": "Violet",
			"info": "At standard temperature and pressure, the density of carbon dioxide is around 1.98 kg/m 3, about 1.67 times that of air.",
			"components": [
				["carbon", 2],
				["oxygen", 1],
				["oxygen", 1]
			],
			"connections": [
				{
					"connector": "carbon",
					"connected": "oxygen",
					"bond": "convalent"
				},
				{
					"connector": "carbon",
					"connected": "oxygen",
					"bond": "convalent"
				}
			]
		},
		{
			"name": "hydrogen peroxide",
			"chemicalFormula": "H2O2",
			"colour": "Tomato",
			"info": "Hydrogen peroxide, in its pure form, is a very pale blue liquid, slightly more viscous than water. It is used as an oxidizer, bleaching agent, and antiseptic.",
			"components": [
				["hydrogen", 1],
				["hydrogen", 1],
				["oxygen", 2],
				["oxygen", 2]
			],
			"connections": [
				{
					"connector": "oxygen",
					"connected": "hydrogen",
					"bond": "convalent"
				},
				{
					"connector": "oxygen",
					"connected": "oxygen",
					"bond": "convalent"
				},
				{
					"connector": "oxygen",
					"connected": "hydrogen",
					"bond": "convalent"
				}
			]
		},
		{
			"name": "ethanol",
			"chemicalFormula": "C2H6O",
			"colour": "SpringGreen",
			"info": "Ethanol is an organic chemical compound, that is very flammable and is naturally produced by the fermentation of sugars by yeasts.",
			"components": [
				["carbon", 4],
				["carbon", 4],
				["hydrogen", 1],
				["hydrogen", 1],
				["hydrogen", 1],
				["hydrogen", 1],
				["hydrogen", 1],
				["hydrogen", 1],
				["oxygen", 2]
			],
			"connections": [
				{
					"connector": "carbon",
					"connected": "hydrogen",
					"bond": "convalent"
				},
				{
					"connector": "carbon",
					"connected": "hydrogen",
					"bond": "convalent"
				},
				{
					"connector": "carbon",
					"connected": "hydrogen",
					"bond": "convalent"
				},
				{
					"connector": "carbon",
					"connected": "carbon",
					"bond": "convalent"
				},
				{
					"connector": "carbon",
					"connected": "hydrogen",
					"bond": "convalent"
				},
				{
					"connector": "carbon",
					"connected": "hydrogen",
					"bond": "convalent"
				},
				{
					"connector": "carbon",
					"connected": "oxygen",
					"bond": "convalent"
				},
				{
					"connector": "oxygen",
					"connected": "hydrogen",
					"bond": "convalent"
				}
			]
		},
		{
			"name": "sodium chloride",
			"chemicalFormula": "NaCl",
			"colour": "White",
			"info": "Sodium chlorine (commonly known as salt) is a colourless or white crystalline compound, used in the preservation of food and seasoning.",
			"components": [
				[ "sodium", 1 ],
				[ "sodium", 1 ]
			],
			"connections": [
				{
					"connector": "sodium",
					"connected": "chlorine",
					"bond": "ionic"
				}
			]
		},
		{
			"name": "methane",
			"chemicalFormula": "CH4",
			"colour": "Brown",
			"info": "Methane is a gas that occours abundantly in nature. It is an organic compound and is made of carbon bonded to 4 hydrogen atoms via convalent bonds.",
			"components": [
				[ "carbon", 4 ],
				[ "hydrogen", 1 ],
				[ "hydrogen", 1 ],
				[ "hydrogen", 1 ],
				[ "hydrogen", 1 ]
			],
			"connections": [
				{
					"connector": "carbon",
					"connected": "hydrogen",
					"bond": "convalent"
				},
				{
					"connector": "carbon",
					"connected": "hydrogen",
					"bond": "convalent"
				},
				{
					"connector": "carbon",
					"connected": "hydrogen",
					"bond": "convalent"
				},
				{
					"connector": "carbon",
					"connected": "hydrogen",
					"bonod": "convalent"
				}
			]
		},
		{
			"name": "hydrogen chloride",
			"chemicalFormula": "HCl",
			"colour": "Red",
			"info": "Hydrogen chloride is a colourless gas, and when reacting with water, forms hydrochloric acid which is a very acidic solution.",
			"components": [
				[ "hydrogen", 1 ],
				[ "chlorine", 1 ]
			],
			"connections": [
				{
					"connector": "hydrogen",
					"connected": "chlorine",
					"bond": "ionic"
				}
			]
		},
		{
			"name": "octane",
			"chemicalFormula": "C8H18",
			"colour": "Grey",
			"info": "Octane is commonly used as petrol for commercial vehicles",
			"components": [
				[ "hydrogen", 1 ],
				[ "hydrogen", 1 ],
				[ "hydrogen", 1 ],
				[ "hydrogen", 1 ],
				[ "hydrogen", 1 ],
				[ "hydrogen", 1 ],
				[ "hydrogen", 1 ],
				[ "hydrogen", 1 ],
				[ "hydrogen", 1 ],
				[ "hydrogen", 1 ],
				[ "hydrogen", 1 ],
				[ "hydrogen", 1 ],
				[ "hydrogen", 1 ],
				[ "hydrogen", 1 ],
				[ "hydrogen", 1 ],
				[ "hydrogen", 1 ],
				[ "hydrogen", 1 ],
				[ "hydrogen", 1 ],
				[ "carbon", 4 ],
				[ "carbon", 4 ],
				[ "carbon", 4 ],
				[ "carbon", 4 ],
				[ "carbon", 4 ],
				[ "carbon", 4 ],
				[ "carbon", 4 ],
				[ "carbon", 4 ]
			],
			"connections": [
				{
					"connector": "carbon",
					"connected": "hydrogen",
					"bond": "ionic"
				},
				{
					"connector": "carbon",
					"connected": "hydrogen",
					"bond": "ionic"
				},
				{
					"connector": "carbon",
					"connected": "hydrogen",
					"bond": "ionic"
				},
				{
					"connector": "carbon",
					"connected": "hydrogen",
					"bond": "ionic"
				},
				{
					"connector": "carbon",
					"connected": "hydrogen",
					"bond": "ionic"
				},
				{
					"connector": "carbon",
					"connected": "hydrogen",
					"bond": "ionic"
				},
				{
					"connector": "carbon",
					"connected": "hydrogen",
					"bond": "ionic"
				},
				{
					"connector": "carbon",
					"connected": "hydrogen",
					"bond": "ionic"
				},
				{
					"connector": "carbon",
					"connected": "hydrogen",
					"bond": "ionic"
				},
				{
					"connector": "carbon",
					"connected": "hydrogen",
					"bond": "ionic"
				},
				{
					"connector": "carbon",
					"connected": "hydrogen",
					"bond": "ionic"
				},
				{
					"connector": "carbon",
					"connected": "hydrogen",
					"bond": "ionic"
				},
				{
					"connector": "carbon",
					"connected": "hydrogen",
					"bond": "ionic"
				},
				{
					"connector": "carbon",
					"connected": "hydrogen",
					"bond": "ionic"
				},
				{
					"connector": "carbon",
					"connected": "hydrogen",
					"bond": "ionic"
				},
				{
					"connector": "carbon",
					"connected": "hydrogen",
					"bond": "ionic"
				},
				{
					"connector": "carbon",
					"connected": "hydrogen",
					"bond": "ionic"
				},
				{
					"connector": "carbon",
					"connected": "hydrogen",
					"bond": "ionic"
				},
				{
					"connector": "carbon",
					"connected": "carbon",
					"bond": "ionic"
				},
				{
					"connector": "carbon",
					"connected": "carbon",
					"bond": "ionic"
				},
				{
					"connector": "carbon",
					"connected": "carbon",
					"bond": "ionic"
				},
				{
					"connector": "carbon",
					"connected": "carbon",
					"bond": "ionic"
				},
				{
					"connector": "carbon",
					"connected": "carbon",
					"bond": "ionic"
				},
				{
					"connector": "carbon",
					"connected": "carbon",
					"bond": "ionic"
				},
				{
					"connector": "carbon",
					"connected": "carbon",
					"bond": "ionic"
				}
			]
		}
	]

mixtures = [
		{
      "name": "hydrochloric acid",
      "chemicalFormula": "HCl+H2O",
      "colour": "Red",
      "info": "Hydrochloric acid is an important chemical reagent and industrial chemical, used in the production of polyvinyl chloride for plastic."
    },
    {
      "name": "saltwater",
      "chemicalFormula": "NaCl+H2O",
      "colour": "Lime",
      "info": "Saltwater is naturally occurring and is denser than water."
    }
	]

molecules = [
	    {
      "name": "hydrogen (stable)",
      "chemicalFormula": "H2",
      "colour": "Ivory",
      "info": "Hydrogen  is a colourless, odourless gas. Once ignited, it burns with a pale blue, an almost invisible flame. Hydrogen is lighter than air, so hydrogen baloons will float.",
      "components": [
        [ "hydrogen", 1 ],
        [ "hydrogen", 1 ]
      ],
      "connections": [
        {
          "connector": "hydrogen",
          "connected": "hydrogen",
          "bond": "convalent"
        }
      ]
    },
    {
      "name": "oxygen (stable)",
      "chemicalFormula": "O2",
      "colour": "Aqua",
      "info": "Oxygen. The gas that we all breathe (in its stable form). It gives life to every creature on earth - 2/3 of the human body is made out of oxygen.",
      "components": [
        [ "oxygen", 1 ],
        [ "oxygen", 1 ]
      ],
      "connections": [
        {
          "connector": "oxygen",
          "connected": "oxygen",
          "bond": "convalent"
        }
      ]
    },
    {
      "name": "ozone",
      "chemicalFormula": "O3",
      "colour": "AquaMarine",
      "info": "Ozone is extremely vital for life on earth as the (good) ozone layer protects life from the harmful ultra violet rays that come from the sun.",
      "components": [
        [ "oxygen", 1 ],
        [ "oxygen", 2 ],
        [ "oxygen", 1 ]
      ],
      "connections": [
        {
          "connector": "oxygen",
          "connected": "oxygen",
          "bond": "convalent"
        },
        {
          "connector": "oxygen",
          "connected": "oxygen",
          "bond": "convalent"
        }
      ]
    }
	]

reactions = [
		{
      "reactants": [ "hydrogen chloride", "water" ],
      "products": [ "hydrochloric acid" ]
    },
    {
      "reactants": [ "sodium chloride", "water" ],
      "products": [ "saltwater" ]
    }
	]

class GetElements(Resource):
	def get(self,id):
		if id == "elements":
			return elements,200
		elif id == "compounds":
			return compounds,200
		elif id == "mixtures":
			return mixtures,200
		elif id == "molecules":
			return molecules,200
		elif id == "reactions":
			return reactions,200
		else:
			return f"There is no such thing as {id}.",404

api.add_resource(GetElements, "/periodicSimElements/<string:id>")

if __name__ == "__main__":
	app.run(debug=True)