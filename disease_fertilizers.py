import json
fertilizers ={
    'Mid-Tillering':#1-25 days
    {
        'Nitrogen':
        {
             "critical":
            {
                "type_of_fertilizer": "Nitrogen(kg/m3)",
                "brands":"fertiliser_brands/nitrogen.jpg",
                "amount_of_fertilizer":"46",

            "adequate":
            {
                "type_of_fertilizer": "Nitrogen(kg/m3)",
                "brands":"fertiliser_brands/nitrogen.jpg",
                "amount_of_fertilizer" :(46,52)
                }
            }
        },
        'Phosphorus':
        {
             "critical":
            {
                "type_of_fertilizer": "phosphorus(kg/m3)",
                "brands":"fertiliser_brands/phosphorus.jpg",
                "amount_of_fertilizer":"1",

            "adequate":
            {
                "type_of_fertilizer": "kg/m3)",
                "brands":"fertiliser_brands/phosphorus.jpg",
                "amount_of_fertilizer":(1,1.8)
                }
            }
        },
        'Potassium':
        {
             "critical":
            {
                "type_of_fertilizer": "potassium(kg/m3)",
                "brands":"fertiliser_brands/potassium.jpg",
                "amount_of_fertilizer":"14",

            "adequate":
            {
                "type_of_fertilizer": "Potassium(kg/m3)",
                "brands":"fertiliser_brands/potassium.jpg",
                "amount_of_fertilizer":(14,28)
                }
            }
        },
        'zinc':
        {
                "critical":
                {
                    
                    "type_of_fertilizer": "zinc(kg/m3)",
                    "brands":"fertiliser_brands/zinc.jpg",
                    "amount_of_fertilizer":"200",

                "adequate":
                {
                    "type_of_fertilizer": "zinc(kg/m3)",
                    "brands":"fertiliser_brands/zinc.jpg",
                    "amount_of_fertilizer":(200, 800)
                    }
                }
            },
    'Maximum-Tillering':#25-27 days
    {
        'Nitrogen':
        {
             "critical":
            {
                "type_of_fertilizer": "Nitrogen(kg/m3)",
                "brands":"fertiliser_brands/nitrogen.jpg",
                "amount_of_fertilizer":"40",

            "adequate":
            {
                "type_of_fertilizer": "Nitrogen(kg/m3)",
                "brands":"fertiliser_brands/nitrogen.jpg",
                "amount_of_fertilizer":(40,46)
                }
            }
        },
        'Phosphorus':
        {
             "critical":
            {
                "type_of_fertilizer": "phosphorus(kg/m3)",
                "brands":"fertiliser_brands/phosphorus.jpg",
                "amount_of_fertilizer":"1",

            "adequate":
            {
                "type_of_fertilizer": "Phosphorus(kg/m3)",
                "brands":"fertiliser_brands/phosphorus.jpg",
                "amount_of_fertilizer":(1,1.8)
                }
            }
        },
        'Potassium':
        {
             "critical":
            {
                "type_of_fertilizer": "potassium(kg/m3)",
                "brands":"fertiliser_brands/potassium.jpg",
                "amount_of_fertilizer":"12",

            "adequate":
            {
                "type_of_fertilizer": "Potassium(kg/m3)",
                "brands":"fertiliser_brands/potassium.jpg",
                "amount_of_fertilizer":(12, 24)
        },
        'zinc':
        {
                "critical":
                {
                    
                    "type_of_fertilizer": "None",
                    "brands":"fertiliser_brands/zinc.jpg",
                    "amount_of_fertilizer":"None",

                "adequate":
                {
                    "type_of_fertilizer": "None",
                    "brands":"fertiliser_brands/zinc.jpg",
                    "amount_of_fertilizer":"None",
                    }
                }
            },
                    
    'Panicle-Initiation':#28-29
    {
        'Nitrogen':
        {
             "critical":
            {
                "type_of_fertilizer": "Nitrogen(kg/m3)",
                "brands":"fertiliser_brands/nitrogen.jpg",
                "amount_of_fertilizer":"33",

            "adequate":
            {
                "type_of_fertilizer": "Nitrogen(kg/m3)",
                "brands":"fertiliser_brands/nitrogen.jpg",
                "amount_of_fertilizer":(33,38)
                }
            }
        },
        'Phosphorus':
        {
             "critical":
            {
                "type_of_fertilizer": "phosphorus(kg/m3)",
                "brands":"fertiliser_brands/phosphorus.jpg",
                "amount_of_fertilizer":"0.8",

            "adequate":
            {
                "type_of_fertilizer": "Phosphorus(kg/m3)",
                "brands":"fertiliser_brands/phosphorus.jpg",
                "amount_of_fertilizer":(1,1.8)
                }
            }
        },
        'Potassium':
        {
             "critical":
            {
                "type_of_fertilizer": "potassium(kg/m3)",
                "brands":"fertiliser_brands/potassium.jpg",
                "amount_of_fertilizer":"11",

            "adequate":
            {
                "type_of_fertilizer": "Potassium(kg/m3)",
                "brands":"fertiliser_brands/potassium.jpg",
                "amount_of_fertilizer":(14,28)
                }
            }
        },
        'zinc':
        {
                   "critical":
                {
                    
                    "type_of_fertilizer": "None",
                    "brands":"fertiliser_brands/zinc.jpg",
                    "amount_of_fertilizer":"None",

                "adequate":
                {
                    "type_of_fertilizer": "None",
                    "brands":"fertiliser_brands/zinc.jpg",
                    "amount_of_fertilizer":"None",
                    }
                }
            }
        },
                    
               
    'Flag-Leaf':#29-105 days
    {
        'Nitrogen':
        {
             "critical":
            {
                "type_of_fertilizer": "Nitrogen(kg/m3)",
                "brands":"fertiliser_brands/nitrogen.jpg",
                "amount_of_fertilizer":"26",

            "adequate":
            {
                "type_of_fertilizer": "Nitrogen(kg/m3)",
                "brands":"fertiliser_brands/nitrogen.jpg",
                "amount_of_fertilizer":(26,32)
                }
            }
        },
        'Phosphorus':
        {
             "critical":
            {
                "type_of_fertilizer": "phosphorus(kg/m3)",
                "brands":"fertiliser_brands/phosphorus.jpg",
                "amount_of_fertilizer":"0.8",

            "adequate":
            {
                "type_of_fertilizer": "Phosphorus(kg/m3)",
                "brands":"fertiliser_brands/phosphorus.jpg",
                "amount_of_fertilizer":(1,1.8)
                }
            }
        },
        'Potassium':
        {
             "critical":
            {
                "type_of_fertilizer": "potassium(kg/m3)",
                "brands":"fertiliser_brands/potassium.jpg",
                "amount_of_fertilizer":"11",

            "adequate":
            {
                "type_of_fertilizer": "Potassium(kg/m3)",
                "brands":"fertiliser_brands/potassium.jpg",
                "amount_of_fertilizer":(12,24)
                }
            }
        },
        'zinc':
        {
                   "critical":
                {
                    
                    "type_of_fertilizer": "None",
                    "brands":"fertiliser_brands/zinc.jpg",
                    "amount_of_fertilizer":"None",

                "adequate":
                {
                    "type_of_fertilizer": "None",
                    "brands":"fertiliser_brands/zinc.jpg",
                    "amount_of_fertilizer":"None",
                    }
                }
        }
    }
                
with open('fertilizers.json', 'w') as f:
    json.dump(fertilizers, f)
