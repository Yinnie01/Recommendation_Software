from trees_module import TreeNode

# Making a Tree of Clothing Category - BAGS 

# {'Bags': set({'Backpacks': [{'Design': 'ASOS DESIGN soft backpack with zip', 'Color': 'Black', 'Price': 'USD 38.00'}, 
#                                                {'Design': 'BASIC PLEASURE drawstring backpack', 'Color': 'Khaki', 'Price': 'USD 42.64'}], 
#                                  'Bum Bags': [{'Design': 'POLO RALPH LAUREN bum bag with pony logo', 'Color': 'Yellow', 'Price': 'USD 119.00'}, 
#                                                {'Design': 'CHAMPION bum bag', 'Color': 'Beige', 'Price': 'USD 23.00'}], 
#                                  'Wallets': [{'Design': 'LOVE MOSCHINO quilted wallet', 'Color': 'Purple', 'Price': 'USD 48.70'}, 
#                                                {'Design': 'ARMANI EA7 logo zip around wallet', 'Color': 'White', 'Price': 'USD 76.04'}], 
#                                  'Clutch bags': [{'Design': 'ASOS DESIGN tassel clutch bag', 'Color': 'Sage', 'Price': 'USD 36.32'}, 
#                                                {'Design': 'ALDO beaded miniball grab bag', 'Color': 'Gold', 'Price': 'USD 37.00'}], 
#                                  'Sling bags': [{'Design': 'ARTSAC Jaspar triple pocket cross body bag', 'Color': 'Stone', 'Price': 'USD 47.37'}, 
#                                                {'Design': 'TOMMY HILFIGER jeans flag logo sling bag', 'Color': 'Cream', 'Price': 'USD 190.00'}]}),

#Root Node
bags = TreeNode("Bags")
#Children Nodes
backpacks = TreeNode("Backpacks")
backpacks_1 = TreeNode("First option")
backpacks_2 = TreeNode("Second option")
bum_bags = TreeNode("Bum Bags")
bum_bags_1 = TreeNode("First option")
bum_bags_2 = TreeNode("Second option")
wallets = TreeNode("Wallets")
wallets_1 = TreeNode("First option")
wallets_2 = TreeNode("Second option")
clutch_bags = TreeNode("Clutch bags")
clutch_bags_1 = TreeNode("First option")
clutch_bags_2 = TreeNode("Second option")
sling_bags = TreeNode("Sling bags")
sling_bags_1 = TreeNode("First option")
sling_bags_2 = TreeNode("Second option")
#Design Leaf Nodes
backpacks_design_1 = TreeNode("ASOS DESIGN soft backpack with zip")
backpacks_design_2 = TreeNode("BASIC PLEASURE drawstring backpack")
bum_bags_design_1 = TreeNode("POLO RALPH LAUREN bum bag with pony logo")
bum_bags_design_2 = TreeNode("CHAMPION bum bag")
wallets_design_1 = TreeNode("LOVE MOSCHINO quilted wallet")
wallets_design_2 = TreeNode("ARMANI EA7 logo zip around wallet")
clutch_bags_design_1 = TreeNode("ASOS DESIGN tassel clutch bag")
clutch_bags_design_2 = TreeNode("ALDO beaded miniball grab bag")
sling_bags_design_1 = TreeNode("ARTSAC Jaspar triple pocket cross body bag")
sling_bags_design_2 = TreeNode("TOMMY HILFIGER jeans flag logo sling bag")
#Color Leaf Nodes
backpacks_color_1 = TreeNode("Black")
backpacks_color_2 = TreeNode("Khaki")
bum_bags_color_1 = TreeNode("Yellow")
bum_bags_color_2 = TreeNode("Beige")
wallets_color_1 = TreeNode("Purple")
wallets_color_2 = TreeNode("White")
clutch_bags_color_1 = TreeNode("Sage")
clutch_bags_color_2 = TreeNode("Gold")
sling_bags_color_1 = TreeNode("Stone")
sling_bags_color_2 = TreeNode("Cream")
#Price Leaf Nodes
backpacks_price_1 = TreeNode(38.00)
backpacks_price_2 = TreeNode(42.64)
bum_bags_price_1 = TreeNode(119.00)
bum_bags_price_2 = TreeNode(23.00)
wallets_price_1 = TreeNode(48.70)
wallets_price_2 = TreeNode(76.04)
clutch_bags_price_1 = TreeNode(36.32)
clutch_bags_price_2 = TreeNode(37.00)
sling_bags_price_1 = TreeNode(57.37)
sling_bags_price_2 = TreeNode(190.00)
#Building the tree
bags.add_child(backpacks,bum_bags,wallets,clutch_bags,sling_bags)
backpacks.add_child(backpacks_1, backpacks_2)
bum_bags.add_child(bum_bags_1, bum_bags_2)
wallets.add_child(wallets_1, wallets_2)
clutch_bags.add_child(clutch_bags_1, clutch_bags_2)
sling_bags.add_child(sling_bags_1, sling_bags_2)
backpacks_1.add_child(backpacks_design_1, backpacks_color_1, backpacks_price_1)
backpacks_2.add_child(backpacks_design_2, backpacks_color_2, backpacks_price_2)
bum_bags_1.add_child(bum_bags_design_1, bum_bags_price_1, bum_bags_color_1)
bum_bags_2.add_child(bum_bags_design_2, bum_bags_price_2, bum_bags_color_2)
wallets_1.add_child(wallets_design_1, wallets_color_1, wallets_price_1)
wallets_2.add_child(wallets_design_2, wallets_color_2, wallets_price_2)
clutch_bags_1.add_child(clutch_bags_design_1, clutch_bags_color_1, clutch_bags_price_1)
clutch_bags_2.add_child(clutch_bags_design_2, clutch_bags_color_2, clutch_bags_price_2)
sling_bags_1.add_child(sling_bags_design_1, sling_bags_color_1, sling_bags_price_1)
sling_bags_2.add_child(sling_bags_design_2, sling_bags_color_2, sling_bags_price_2)

# Making a Tree of Clothing Category - DRESSES

# 'Dresses': set({'Wrap dresses': [{'Design': 'ASOS DESIGN wrap balloon sleeve midi dress', 'Color': 'Black', 'Price': 'USD 32.06'}, 
#                                                {'Design': 'GEORGIA LOUISE satin ruffle hem', 'Color': 'Pink', 'Price': 'USD 31.58'}],
#                             'Trapeze dresses': [{'Design': 'ASOS DESIGN tall highneck pleated trapeze mini dress', 'Color': 'Mint', 'Price': 'USD 26.84'}, 
#                                                {'Design': 'WHISTLES mini trapeze dress in green floral', 'Color': 'Floral', 'Price': 'USD 192.64'}],
#                             'Bandeau dresses': [{'Design': 'ARIA COVE bandeau plunge wire maxi dress', 'Color': 'Aqua', 'Price': 'USD 21.32'}, 
#                                                {'Design': 'LACE and BEADS tulle bandeau mini dress', 'Color': 'Mangenta', 'Price': 'USD 133.00'}],
#                             'Fish tail dresses': [{'Design': 'GODDOVA BARDOT fishtail maxi dress', 'Color': 'Powder Blue', 'Price': 'USD 41.85'}, 
#                                                {'Design': 'MAYA BRIDAL embellished fishtail maxi dress', 'Color': 'Ivory', 'Price': 'USD 266.00'}],
#                             'Jumper dresses': [{'Design': 'THREADBARE Petite Parker off shoulder', 'Color': 'Taupe', 'Price': 'USD 22.90'}, 
#                                                {'Design': 'WEDNESDAYS GIRL chunky rib zip through funnel dress ', 'Color': 'Ivory', 'Price': 'USD 26.84'}]})

# Root Node
dresses = TreeNode("Dresses")
#Children Nodes
wrap_dresses = TreeNode("Wrap Dresses")
wrap_dresses_1 = TreeNode("First option")
wrap_dresses_2 = TreeNode("Second option")
trapeze_dresses = TreeNode("Trapeze Dresses")
trapeze_dresses_1 = TreeNode("First option")
trapeze_dresses_2 = TreeNode("Second option")
bandeau_dresses = TreeNode("Bandeau Dresses")
bandeau_dresses_1 = TreeNode("First option")
bandeau_dresses_2 = TreeNode("Second option")
fish_tail_dresses = TreeNode("Fish Tail Dresses")
fish_tail_dressess_1 = TreeNode("First option")
fish_tail_dresses_2 = TreeNode("Second option")
jumper_dresses = TreeNode("Jumper Dresses")
jumper_dresses_1 = TreeNode("First option")
jumper_dresses_2 = TreeNode("Second option")
#Design Leaf Nodes
wrap_dresses_design_1 = TreeNode("ASOS DESIGN wrap balloon sleeve midi dress")
wrap_dresses_design_2 = TreeNode("GEORGIA LOUISE satin ruffle hem")
trapeze_dresses_design_1 = TreeNode("ASOS DESIGN tall highneck pleated trapeze mini dress")
trapeze_dresses_design_2 = TreeNode("WHISTLES mini trapeze dress in green floral")
bandeau_dresses_design_1 = TreeNode("ARIA COVE bandeau plunge wire maxi dress")
bandeau_dresses_design_2 = TreeNode("LACE and BEADS tulle bandeau mini dress")
fish_tail_dresses_design_1 = TreeNode("GODDOVA BARDOT fishtail maxi dress")
fish_tail_dresses_design_2 = TreeNode("MAYA BRIDAL embellished fishtail maxi dress")
jumper_dresses_design_1 = TreeNode("THREADBARE Petite Parker off shoulder")
jumper_dresses_design_2 = TreeNode("WEDNESDAYS GIRL chunky rib zip through funnel dress")
#Color Leaf Nodes
wrap_dresses_color_1 = TreeNode("Black")
wrap_dresses_color_2 = TreeNode("Pink")
trapeze_dresses_color_1 = TreeNode("Mint")
trapeze_dresses_color_2 = TreeNode("Floral")
bandeau_dresses_color_1 = TreeNode("Aqua")
bandeau_dresses_color_2 = TreeNode("Mangenta")
fish_tail_dresses_color_1 = TreeNode("Powder Blue")
fish_tail_dresses_color_2 = TreeNode("Ivory")
jumper_dresses_color_1 = TreeNode("Taupe")
jumper_dresses_color_2 = TreeNode("Cream")
#Price Leaf Nodes
wrap_dresses_price_1 = TreeNode(32.06)
wrap_dresses_price_2 = TreeNode(41.58)
trapeze_dresses_price_1 = TreeNode(26.84)
trapeze_dresses_price_2 = TreeNode(192.64)
bandeau_dresses_price_1 = TreeNode(21.32)
bandeau_dresses_price_2 = TreeNode(133.00)
fish_tail_dresses_price_1 = TreeNode(41.85)
fish_tail_dresses_price_2 = TreeNode(266.00)
jumper_dresses_price_1 = TreeNode(52.90)
jumper_dresses_price_2 = TreeNode(26.84)
# Building the Tree
dresses.add_child(wrap_dresses, trapeze_dresses, bandeau_dresses, fish_tail_dresses, jumper_dresses)
wrap_dresses.add_child(wrap_dresses_1, wrap_dresses_2)
trapeze_dresses.add_child(trapeze_dresses_1, trapeze_dresses_2)
bandeau_dresses.add_child(bandeau_dresses_1, bandeau_dresses_2)
fish_tail_dresses.add_child(fish_tail_dressess_1, fish_tail_dresses_2)
jumper_dresses.add_child(jumper_dresses_1, jumper_dresses_2)
wrap_dresses_1.add_child(wrap_dresses_design_1, wrap_dresses_color_1, wrap_dresses_price_1)
wrap_dresses_2.add_child(wrap_dresses_design_2, wrap_dresses_color_2, wrap_dresses_price_2)
trapeze_dresses_1.add_child(trapeze_dresses_design_1, trapeze_dresses_color_1, trapeze_dresses_price_1)
trapeze_dresses_2.add_child(trapeze_dresses_design_2, trapeze_dresses_color_2, trapeze_dresses_price_2)
bandeau_dresses_1.add_child(bandeau_dresses_design_1, bandeau_dresses_color_1, bandeau_dresses_price_1)
bandeau_dresses_2.add_child(bandeau_dresses_design_2, bandeau_dresses_color_2, bandeau_dresses_price_2)
fish_tail_dressess_1.add_child(fish_tail_dresses_design_1, fish_tail_dresses_color_1, fish_tail_dresses_price_1)
fish_tail_dresses_2.add_child(fish_tail_dresses_design_2, fish_tail_dresses_color_2, fish_tail_dresses_price_2)
jumper_dresses_1.add_child(jumper_dresses_design_1, jumper_dresses_color_1, jumper_dresses_price_1)
jumper_dresses_2.add_child(jumper_dresses_design_2, jumper_dresses_color_2, jumper_dresses_price_2)


# Making a Tree of Clothing Category - FOOTWEAR

# 'Footwear': set({'Sneakers': [{'Design': 'NEW BALANCE 610 trainers', 'Color': 'Green', 'Price': 'USD 174.00'}, 
#                                                {'Design': 'ADIDAS Originals', 'Color': 'Cream and Black', 'Price': 'USD 143.00'}],
#                              'Sandals': [{'Design': 'TOP SHOP Rosie ankle tie strippy sandal', 'Color': 'Blue', 'Price': 'USD 20.83'}, 
#                                                {'Design': 'PUBLIC DESIRE Wide Fit platform sandals', 'Color': 'Pink', 'Price': 'USD 19.64'}],
#                              'Heels': [{'Design': 'BEBO Mariya bridal pearl high heeled clear shoe', 'Color': 'White', 'Price': 'USD 21.32'}, 
#                                                {'Design': 'ASOS DESIGN Nation stiletto heels', 'Color': 'Brown', 'Price': 'USD 28.42'}],
#                              'Chelsea Boots': [{'Design': 'ASOS DESIGN Anthem chunky chelsea boots', 'Color': 'Off-white', 'Price': 'USD 22.42'}, 
#                                                {'Design': 'TRUFFLE COLLECTION chelsea boots with gold trim', 'Color': 'Black Croc', 'Price': 'USD 48.00'}],
#                              'Loafers': [{'Design': 'DAISY STREET Exclusive double heeled loafers', 'Color': 'Lavender', 'Price': 'USD 25.24'}, 
#                                                {'Design': 'RIVER ISLAND chunky snaffle loafer', 'Color': 'Red', 'Price': 'USD 61.00'}]})

# Root Node
footwear = TreeNode("Footwear")
#Children Nodes
sneakers = TreeNode("Sneakers")
sneakers_1 = TreeNode("First option")
sneakers_2 = TreeNode("Second option")
sandals = TreeNode("Sandals")
sandals_1 = TreeNode("First option")
sandals_2 = TreeNode("Second option")
heels = TreeNode("Heels")
heels_1 = TreeNode("First option")
heels_2 = TreeNode("Second option")
chelsea_boots = TreeNode("Chelsea Boots")
chelsea_boots_1 = TreeNode("First option")
chelsea_boots_2 = TreeNode("Second option")
loafers = TreeNode("Loafers")
loafers_1 = TreeNode("First option")
loafers_2 = TreeNode("Second option")
#Design Leaf Nodes
sneakers_design_1 = TreeNode("NEW BALANCE 610 trainers")
sneakers_design_2 = TreeNode("ADIDAS Originals")
sandals_design_1 = TreeNode("TOP SHOP Rosie ankle tie strippy sandal")
sandals_design_2 = TreeNode("PUBLIC DESIRE Wide Fit platform sandals")
heels_design_1 = TreeNode("BEBO Mariya bridal pearl high heeled clear shoe")
heels_design_2 = TreeNode("ASOS DESIGN Nation stiletto heels")
chelsea_boots_design_1 = TreeNode("ASOS DESIGN Anthem chunky chelsea boots")
chelsea_boots_design_2 = TreeNode("TRUFFLE COLLECTION chelsea boots with gold trim")
loafers_design_1 = TreeNode("DAISY STREET Exclusive double heeled loafers")
loafers_design_2 = TreeNode("RIVER ISLAND chunky snaffle loafer")
#Color Leaf Nodes
sneakers_color_1 = TreeNode("Green")
sneakers_color_2 = TreeNode("Cream and Black")
sandals_color_1 = TreeNode("Blue")
sandalss_color_2 = TreeNode("Pink")
heels_color_1 = TreeNode("White")
heels_color_2 = TreeNode("Brown")
chelsea_boots_color_1 = TreeNode("Off white")
chelsea_boots_color_2 = TreeNode("Black Croc")
loafers_color_1 = TreeNode("Lavender")
loafers_color_2 = TreeNode("Red")
#Price Leaf Nodes
sneakers_price_1 = TreeNode(174.00)
sneakers_price_2 = TreeNode(143.00)
sandals_price_1 = TreeNode(20.83)
sandals_price_2 = TreeNode(19.64)
heels_price_1 = TreeNode(21.32)
heels_price_2 = TreeNode(28.42)
chelsea_boots_price_1 = TreeNode(22.42)
chelsea_boots_price_2 = TreeNode(48.00)
loafers_price_1 = TreeNode(25.24)
loafers_price_2 = TreeNode(61.00)
# Building the tree
footwear.add_child(sneakers, sandals, heels, chelsea_boots, loafers)
sneakers.add_child(sneakers_1, sneakers_2)
sandals.add_child(sandals_1, sandals_2)
heels.add_child(heels_1, heels_2)
chelsea_boots.add_child(chelsea_boots_1, chelsea_boots_2)
loafers.add_child(loafers_1, loafers_2)
sneakers_1.add_child(sneakers_design_1, sneakers_color_1, sneakers_price_1)
sneakers_2.add_child(sneakers_design_2, sneakers_color_2, sneakers_price_2)
sandals_1.add_child(sandals_design_1, sandals_color_1, sandals_price_1)
sandals_2.add_child(sandals_design_2, sandalss_color_2, sandals_price_2)
heels_1.add_child(heels_design_1, heels_color_1, heels_price_1)
heels_2.add_child(heels_design_2, heels_color_2, heels_price_2)
chelsea_boots_1.add_child(chelsea_boots_design_1, chelsea_boots_color_1, chelsea_boots_price_1)
chelsea_boots_2.add_child(chelsea_boots_design_2, chelsea_boots_color_2, chelsea_boots_price_2)
loafers_1.add_child(loafers_design_1,loafers_color_1, loafers_price_1)
loafers_2.add_child(loafers_design_2,loafers_color_2, loafers_price_2)


# Making a Tree of Clothing Category - ACCESSORIES

#  'Accessories': set({'Neck pieces': [{'Design': 'DESIGN B London layered pearl neck lace', 'Color': 'Off-white', 'Price': 'USD 17.00'}, 
#                                                {'Design': 'ASOS DESIGN chocker necklace with wide crystals', 'Color': 'Silver', 'Price': 'USD 31.00'}],
#                                 'Scarves': [{'Design': 'RECLAIMED Vintage sequin scarf', 'Color': 'Silver', 'Price': 'USD 18.16'}, 
#                                                {'Design': 'MY ACCESSORIES shimmer lighweight scarf', 'Color': 'Brown', 'Price': 'USD 16.00'}],
#                                 'Finger Rings': [{'Design': 'ASOS DESIGN stacked ring with molten design', 'Color': 'Black', 'Price': 'USD 12.42'}, 
#                                                {'Design': 'WHISTLES statement buckle ring', 'Color': 'Gold', 'Price': 'USD 10.50'}],
#                                 'Earrings': [{'Design': 'ASOS DESIGN stud earrings with long drop design', 'Color': 'Red', 'Price': 'USD 13.52'}, 
#                                                {'Design': 'DESIGN B London oversized stud earrings', 'Color': 'Mint', 'Price': 'USD 20.00'}],
#                                 'Anklets': [{'Design': 'ASOS DESIGN anklet with faux pearl and crytal cupchain', 'Color': 'Green', 'Price': 'USD 26.90'}, 
#                                                {'Design': 'ALDO single anklet with hanging balls', 'Color': 'Gold', 'Price': 'USD 48.00'}]})

# Root Node
accessories = TreeNode("Accessories")
#Children Nodes
neckpieces = TreeNode("Neck Pieces")
neckpieces_1 = TreeNode("First option")
neckpieces_2 = TreeNode("Second option")
scarves = TreeNode("Scarves")
scarves_1 = TreeNode("First option")
scarves_2 = TreeNode("Second option")
finger_rings = TreeNode("Finger Rings")
finger_rings_1 = TreeNode("First option")
finger_rings_2 = TreeNode("Second option")
earrings = TreeNode("Earrings")
earrings_1 = TreeNode("First option")
earrings_2 = TreeNode("Second option")
anklets = TreeNode("Anklets")
anklets_1 = TreeNode("First option")
anklets_2 = TreeNode("Second option")
#Design Leaf Nodes
neckpieces_design_1 = TreeNode("DESIGN B London layered pearl neck lace")
neckpieces_design_2 = TreeNode("ASOS DESIGN chocker necklace with wide crystals")
scarves_design_1 = TreeNode("RECLAIMED Vintage sequin scarf")
scarves_design_2 = TreeNode("MY ACCESSORIES shimmer lighweight scarf")
finger_rings_design_1 = TreeNode("ASOS DESIGN stacked ring with molten design")
finger_rings_design_2 = TreeNode("WHISTLES statement buckle ring")
earrings_design_1 = TreeNode("ASOS DESIGN stud earrings with long drop design")
earrings_design_2 = TreeNode("DESIGN B London oversized stud earrings")
anklets_design_1 = TreeNode("ASOS DESIGN anklet with faux pearl and crytal cupchain")
anklets_design_2 = TreeNode("ALDO single anklet with hanging balls")
#Color Leaf Nodes
neckpieces_color_1 = TreeNode("Taupe")
neckpieces_color_2 = TreeNode("Silver")
scarves_color_1 = TreeNode("Silver")
scarves_color_2 = TreeNode("Brown")
finger_rings_color_1 = TreeNode("Black")
finger_rings_color_2 = TreeNode("Gold")
earrings_color_1 = TreeNode("Red")
earrings_color_2 = TreeNode("Mint")
anklets_color_1 = TreeNode("Green")
anklets_color_2 = TreeNode("Gold")
#Price Leaf Nodes
neckpieces_price_1 = TreeNode(74.00)
neckpieces_price_2 = TreeNode(31.00)
scarvess_price_1 = TreeNode(18.16)
scarves_price_2 = TreeNode(16.00)
finger_rings_price_1 = TreeNode(12.42)
finger_rings_price_2 = TreeNode(10.50)
earrings_price_1 = TreeNode(13.52)
earrings_price_2 = TreeNode(20.00)
anklets_price_1 = TreeNode(26.90)
anklets_price_2 = TreeNode(48.00)
# Building the tree
accessories.add_child(neckpieces, scarves, finger_rings, earrings, anklets)
neckpieces.add_child(neckpieces_1, neckpieces_2)
neckpieces_1.add_child(neckpieces_design_1, neckpieces_color_1, neckpieces_price_1)
neckpieces_2.add_child(neckpieces_design_2, neckpieces_color_2, neckpieces_price_2)
scarves.add_child(scarves_1, scarves_2)
scarves_1.add_child(scarves_design_1, scarves_color_1, scarvess_price_1)
scarves_2.add_child(scarves_design_2, scarves_color_2, scarves_price_2)
finger_rings.add_child(finger_rings_1, finger_rings_2)
finger_rings_1.add_child(finger_rings_design_1, finger_rings_color_1, finger_rings_price_1)
finger_rings_2.add_child(finger_rings_design_2, finger_rings_color_2, finger_rings_price_2)
earrings.add_child(earrings_1, earrings_2)
earrings_1.add_child(earrings_design_1, earrings_color_1, earrings_price_1)
earrings_2.add_child(earrings_design_1, earrings_color_1,earrings_price_1)
anklets.add_child(anklets_1, anklets_2)
anklets_1.add_child(anklets_design_1, anklets_color_1, anklets_price_1)
anklets_2.add_child(anklets_design_2, anklets_color_2, anklets_price_2)


# Making a Tree of Clothing Category - TOPS

# 'Tops': set({'Polo-shirts': [{'Design': 'ADIDAS Originals 70s stripe polo shirt', 'Color': 'Dark Green', 'Price': 'USD 44.20'}, 
#                                                {'Design': 'PINKIE Wrap front polo oversized long sleeve', 'Color': 'Blue', 'Price': 'USD 17.37'}],
#                          'Crop Tops': [{'Design': 'TRUE NORTH Face cropped tank top', 'Color': 'White', 'Price': 'USD 34.74'}, 
#                                                {'Design': 'ONLY Executive halter neck top', 'Color': 'Purple', 'Price': 'USD 16.58'}],
#                          'Corset Tops': [{'Design': 'LOLA MAY Tall Satin corset crop top', 'Color': 'Brown', 'Price': 'USD 9.47'}, 
#                                                {'Design': 'ASOS DESIGN bandeau corset with hook and eye', 'Color': 'Berry', 'Price': 'USD 24.48'}],
#                          'Kimonos': [{'Design': 'BRAVE SOUL Plus Maxi beach kimono', 'Color': 'Green and Pink', 'Price': 'USD 23.69'}, 
#                                                {'Design': 'ASOS DESIGN Maxi beach kimono', 'Color': 'Magenta', 'Price': 'USD 31.00'}],
#                          'Bodies': [{'Design': 'UNIQUE 21 Petite plunge tailored bodysuit', 'Color': 'Pink', 'Price': 'USD 21.32'}, 
#                                                {'Design': 'STRADIVARIUS Off Shoulder bodysuit with twist bust', 'Color': 'Black', 'Price': 'USD 7.90'}]})

# Root Node
tops = TreeNode("Tops")
#Children Nodes
polo_shirts = TreeNode("Polo Shirts")
polo_shirts_1 = TreeNode("First option")
polo_shirts_2 = TreeNode("Second option")
crop_tops = TreeNode("Crop Tops")
crop_tops_1 = TreeNode("First option")
crop_tops_2 = TreeNode("Second option")
corsets = TreeNode("Corset Tops")
corsets_1 = TreeNode("First option")
corsets_2 = TreeNode("Second option")
kimonos = TreeNode("Kimonos")
kimonos_1 = TreeNode("First option")
kimonos_2 = TreeNode("Second option")
bodies = TreeNode("Bodies")
bodies_1 = TreeNode("First option")
bodies_2 = TreeNode("Second option")
#Design Leaf Nodes
polo_shirts_design_1 = TreeNode("ADIDAS Originals 70s stripe polo shirt")
polo_shirts_design_2 = TreeNode("PINKIE Wrap front polo oversized long sleeve")
crop_tops_design_1 = TreeNode("TRUE NORTH Face cropped tank top")
crop_tops_design_2 = TreeNode("ONLY Executive halter neck crop top")
corsets_design_1 = TreeNode("LOLA MAY Tall Satin corset crop top")
corsets_design_2 = TreeNode("ASOS DESIGN bandeau corset with hook and eye")
kimonos_design_1 = TreeNode("BRAVE SOUL Plus Maxi beach kimono")
kimonos_design_2 = TreeNode("ASOS DESIGN Maxi beach kimono")
bodies_design_1 = TreeNode("UNIQUE 21 Petite plunge tailored bodysuit")
bodies__design_2 = TreeNode("STRADIVARIUS Off Shoulder bodysuit with twist bust")
#Color Leaf Nodes
polo_shirts_color_1 = TreeNode("Dark Green")
polo_shirts_color_2 = TreeNode("Blue")
crop_tops_color_1 = TreeNode("White")
crop_tops_color_2 = TreeNode("Purple")
corsets_color_1 = TreeNode("Brown")
corsets_color_2 = TreeNode("Berry")
kimonos_color_1 = TreeNode("Green and Pink")
kimonos_color_2 = TreeNode("Magenta")
bodies_color_1 = TreeNode("Pink")
bodies_color_2 = TreeNode("Black")
#Price Leaf Nodes
polo_shirts_price_1 = TreeNode(44.20)
polo_shirts_price_2 = TreeNode(17.37)
crop_tops_price_1 = TreeNode(34.74)
crop_tops_price_2 = TreeNode(16.58)
corsets_price_1 = TreeNode(9.47)
corsets_price_2 = TreeNode(24.48)
kimonos_price_1 = TreeNode(23.69)
kimonos_price_2 = TreeNode(31.00)
bodies_price_1 = TreeNode(21.32)
bodies_price_2 = TreeNode(7.90)
# Building the tree
tops.add_child(polo_shirts, crop_tops, corsets, kimonos, bodies)
polo_shirts.add_child(polo_shirts_1, polo_shirts_2)
crop_tops.add_child(crop_tops_1, crop_tops_2)
corsets.add_child(corsets_1, corsets_2)
kimonos.add_child(kimonos_1, kimonos_2)
bodies.add_child(bodies_1, bodies_2)
polo_shirts_1.add_child(polo_shirts_design_1, polo_shirts_color_1, polo_shirts_price_1)
polo_shirts_2.add_child(polo_shirts_design_2, polo_shirts_color_2, polo_shirts_price_2)
crop_tops_1.add_child(crop_tops_design_1, crop_tops_color_1, crop_tops_price_1)
crop_tops_2.add_child(crop_tops_design_2, crop_tops_color_2, crop_tops_price_2)
corsets_1.add_child(corsets_design_1, corsets_color_1, corsets_price_1)
corsets_2.add_child(corsets_design_2, corsets_color_2, corsets_price_2)
kimonos_1.add_child(kimonos_design_1, kimonos_color_1, kimonos_price_1)
kimonos_2.add_child(kimonos_design_2, kimonos_color_2, kimonos_price_2)
bodies_1.add_child(bodies_design_1, bodies_color_1, bodies_price_1)
bodies_2.add_child(bodies__design_2, bodies_color_2, bodies_price_2)


# Making a Tree of Clothing Category - JEANS TROUSERS

# 'Jeans Trousers': set({'Skinny jeans': [{'Design': 'DTT Chloe disco stretch skinny jeans', 'Color': 'Mid wash blue', 'Price': 'USD 15.79'}, 
#                                                {'Design': 'STRADIVARIUS Tall super skinny jeans', 'Color': 'Grey', 'Price': 'USD 11.05'}],
#                                    'High Waisted jeans': [{'Design': 'PULL & BEAR High waisted jeans', 'Color': 'Medium Blue', 'Price': 'USD 22.90'}, 
#                                                {'Design': 'ASOS DESIGN Hourglass high waisted jeans', 'Color': 'Berry', 'Price': 'USD 45.37'}],
#                                    'Shorts': [{'Design': 'NOISY MAY Tall Frayed hem longline denim', 'Color': 'Black', 'Price': 'USD 17.20'}, 
#                                                {'Design': 'DTT Petite skinny denim shorts', 'Color': 'Grey', 'Price': 'USD 12.63'}],
#                                    'Flared jeans': [{'Design': 'ASOS DESIGN kickflare jeans in pinstripe', 'Color': 'Grey', 'Price': 'USD 28.42'}, 
#                                                {'Design': 'URBAN REVIVO flare jeans', 'Color': 'Blue', 'Price': 'USD 53.00'}],
#                                    'Ripped jeans': [{'Design': 'PARISIAN Tall Skinny jeans with rips', 'Color': 'Mid wash blue', 'Price': 'USD 22.11'}, 
#                                                {'Design': 'STRADIVARIUS jeans with ripped knee', 'Color': 'Green', 'Price': 'USD 26.84'}]}),
# Root Node
jeans_trousers = TreeNode("Jeans Trousers")
#Children Nodes
skinny_jeans = TreeNode("Skinny Jeans")
skinny_jeans_1 = TreeNode("First option")
skinny_jeans_2 = TreeNode("Second option")
high_waisted = TreeNode("High Waisted Jeans")
high_waisted_1 = TreeNode("First option")
high_waisted_2 = TreeNode("Second option")
shorts = TreeNode("Jeans Shorts")
shorts_1 = TreeNode("First option")
shorts_2 = TreeNode("Second option")
flared_jeans = TreeNode("Flared Jeans")
flared_jeans_1 = TreeNode("First option")
flared_jeans_2 = TreeNode("Second option")
ripped_jeans = TreeNode("Ripped Jeans")
ripped_jeans_1 = TreeNode("First option")
ripped_jeans_2 = TreeNode("Second option")
#Design Leaf Nodes
skinny_jeans_design_1 = TreeNode("DTT Chloe disco stretch skinny jeans")
skinny_jeans_design_2 = TreeNode("STRADIVARIUS Tall super skinny jeans")
high_waisted_design_1 = TreeNode("PULL & BEAR High waisted jeans")
high_waisted_design_2 = TreeNode("ASOS DESIGN Hourglass high waisted jeans")
shorts_design_1 = TreeNode("NOISY MAY Tall Frayed hem longline denim")
shorts_design_2 = TreeNode("DTT Petite skinny denim shorts")
flared_jeans_design_1 = TreeNode("ASOS DESIGN kickflare jeans in pinstripe")
flared_jeans_design_2 = TreeNode("URBAN REVIVO flare jeans")
ripped_jeans_design_1 = TreeNode("PARISIAN Tall Skinny jeans with rips")
ripped_jeans__design_2 = TreeNode("STRADIVARIUS jeans with ripped knee")
#Color Leaf Nodes
skinny_jeans_color_1 = TreeNode("Mid wash blue")
skinny_jeans_color_2 = TreeNode("Grey")
high_waisteds_color_1 = TreeNode("Medium Blue")
high_waisted_color_2 = TreeNode("Berry")
shorts_color_1 = TreeNode("Black")
shorts_color_2 = TreeNode("Grey")
flared_jeans_color_1 = TreeNode("Taupe")
flared_jeans_color_2 = TreeNode("Blue")
ripped_jeans_color_1 = TreeNode("Off white")
ripped_jeans_color_2 = TreeNode("Green")
#Price Leaf Nodes
skinny_jeans_price_1 = TreeNode(15.79)
skinny_jeans_price_2 = TreeNode(11.05)
high_waisted_price_1 = TreeNode(22.90)
high_waisted_price_2 = TreeNode(45.37)
shorts_price_1 = TreeNode(17.20)
shorts_price_2 = TreeNode(12.63)
flared_jeans_price_1 = TreeNode(28.42)
flared_jeans_price_2 = TreeNode(53.00)
ripped_jeans_price_1 = TreeNode(22.11)
ripped_jeans_price_2 = TreeNode(26.84)
# Building the tree
jeans_trousers.add_child(skinny_jeans, high_waisted, shorts, flared_jeans, ripped_jeans)
skinny_jeans.add_child(skinny_jeans_1, skinny_jeans_2)
high_waisted.add_child(high_waisted_1, high_waisted_2)
shorts.add_child(shorts_1, shorts_2)
flared_jeans.add_child(flared_jeans_1, flared_jeans_2)
ripped_jeans.add_child(ripped_jeans_1, ripped_jeans_2)
skinny_jeans_1.add_child(skinny_jeans_design_1, skinny_jeans_color_1, skinny_jeans_price_1)
skinny_jeans_2.add_child(skinny_jeans_design_2, skinny_jeans_color_2, skinny_jeans_price_2)
high_waisted_1.add_child(high_waisted_design_1, high_waisteds_color_1, high_waisted_price_1)
high_waisted_2.add_child(high_waisted_design_2, high_waisted_color_2, high_waisted_price_2)
shorts_1.add_child(shorts_design_1, shorts_color_1, shorts_price_1)
shorts_2.add_child(shorts_design_2, shorts_color_2, shorts_price_2)
flared_jeans_1.add_child(flared_jeans_design_1, flared_jeans_color_1, flared_jeans_price_1)
flared_jeans_2.add_child(flared_jeans_design_2, flared_jeans_color_2, flared_jeans_price_2)
ripped_jeans_1.add_child(ripped_jeans_design_1, ripped_jeans_color_1, ripped_jeans_price_1)
ripped_jeans_2.add_child(ripped_jeans__design_2, ripped_jeans_color_2, ripped_jeans_price_2)


# Making a Tree of Clothing Category - SKIRTS

# 'Skirts': set({'Pleated skirts': [{'Design': 'ASOS DESIGN pleated midi skirt', 'Color': 'Baby Pink', 'Price': 'USD 27.63'}, 
#                                                {'Design': 'COLLUSION box pletaed midi skirt with high split', 'Color': 'Berry', 'Price': 'USD 11.05'}],
#                            'A line skirts': [{'Design': 'MISS SELFRIDGE chiffon lace gadet maxi skirt', 'Color': 'Floral', 'Price': 'USD 23.79'}, 
#                                                {'Design': 'BAUUUT Tall Tulle maxi skirt', 'Color': 'Lavender', 'Price': 'USD 26.06'}],
#                            'Bodycon skirts': [{'Design': 'PUBLIC DESIRE faux leather co-ord skirt', 'Color': 'Red', 'Price': 'USD 30.79'}, 
#                                                {'Design': 'FIRE AND GLORY Christine ruched midi skirt', 'Color': 'Brown', 'Price': 'USD 11.05'}],
#                            'Mini skirts': [{'Design': 'MISS EMPIRE knitted mini skirt co-ord', 'Color': 'Cream', 'Price': 'USD 27.00'}, 
#                                                {'Design': 'JDY Frill detail mini skirt in red and pink floral', 'Color': 'Red and Pink', 'Price': 'USD 17.37'}],
#                            'Jipsy skirts': [{'Design': 'LIPSY Jipsy skirt in floral print', 'Color': 'Floral', 'Price': 'USD 31.58'}, 
#                                                {'Design': 'STRADIVARIUS Midi Jipsy skirt in Fuschia', 'Color': 'Fuschia', 'Price': 'USD 37.98'}]})}

# Root Node
skirts = TreeNode("Skirts")
#Children Nodes
pleated_skirts = TreeNode("Pleated Skirts")
pleated_skirts_1 = TreeNode("First option")
pleated_skirts_2 = TreeNode("Second option")
a_line_skirts = TreeNode("A Line Skirts")
a_line_skirts_1 = TreeNode("First option")
a_line_skirts_2 = TreeNode("Second option")
bodycon_skirts = TreeNode("Bodycon Skirts")
bodycon_skirts_1 = TreeNode("First option")
bodycon_skirts_2 = TreeNode("Second option")
mini_skirts = TreeNode("Mini Skirts")
mini_skirts_1 = TreeNode("First option")
mini_skirts_2 = TreeNode("Second option")
jipsy_skirts = TreeNode("Jipsy Skirts")
jipsy_skirts_1 = TreeNode("First option")
jipsy_skirts_2 = TreeNode("Second option")
#Design Leaf Nodes
pleated_skirts_design_1 = TreeNode("ASOS DESIGN pleated midi skirt")
pleated_skirts_design_2 = TreeNode("COLLUSION box pletaed midi skirt with high split")
a_line_skirts_design_1 = TreeNode("MISS SELFRIDGE chiffon lace gadet maxi skirt")
a_line_skirts_design_2 = TreeNode("BEAUUUTT Tall Tulle maxi skirt")
bodycon_skirts_design_1 = TreeNode("PUBLIC DESIRE faux leather co-ord bodycon skirt")
bodycon_skirts_design_2 = TreeNode("FIRE AND GLORY Christine ruched midi bodycon skirt")
mini_skirts_design_1 = TreeNode("MISS EMPIRE knitted mini skirt co-ord")
mini_skirts_design_2 = TreeNode("JDY Frill detail mini skirt in red and pink floral")
jipsy_skirts_design_1 = TreeNode("LIPSY Jipsy skirt in floral print")
jipsy_skirts_design_2 = TreeNode("STRADIVARIUS Midi Jipsy skirt in Fuschia")
#Color Leaf Nodes
pleated_skirts_color_1 = TreeNode("Baby Pink")
pleated_skirts_color_2 = TreeNode("Berry")
a_line_skirts_color_1 = TreeNode("Floral")
a_line_skirts_color_2 = TreeNode("Lavender")
bodycon_skirts_color_1 = TreeNode("Red")
bodycon_skirts_color_2 = TreeNode("Brown")
mini_skirts_color_1 = TreeNode("Cream")
mini_skirts_color_2 = TreeNode("Red and Pink")
jipsy_skirts_color_1 = TreeNode("Floral")
jipsy_skirts_color_2 = TreeNode("Fuschia")
#Price Leaf Nodes
pleated_skirts_price_1 = TreeNode(27.63)
pleated_skirts_price_2 = TreeNode(11.05)
a_line_skirts_price_1 = TreeNode(23.79)
a_line_skirts_price_2 = TreeNode(56.06)
bodycon_skirts_price_1 = TreeNode(30.79)
bodycon_skirts_price_2 = TreeNode(89.63)
mini_skirts_price_1 = TreeNode(27.00)
mini_skirts_price_2 = TreeNode(33.00)
jipsy_skirts_price_1 = TreeNode(31.58)
jipsy_skirts_price_2 = TreeNode(126.74)
# Building the tree
skirts.add_child(pleated_skirts, a_line_skirts, bodycon_skirts, mini_skirts, jipsy_skirts)
pleated_skirts.add_child(pleated_skirts_1, pleated_skirts_2)
a_line_skirts.add_child(a_line_skirts_1, a_line_skirts_2)
bodycon_skirts.add_child(bodycon_skirts_1, bodycon_skirts_2)
mini_skirts.add_child(mini_skirts_1, mini_skirts_2)
jipsy_skirts.add_child(jipsy_skirts_1, jipsy_skirts_2)
pleated_skirts_1.add_child(pleated_skirts_design_1, pleated_skirts_color_1, pleated_skirts_price_1)
pleated_skirts_2.add_child(pleated_skirts_design_2, pleated_skirts_color_2, pleated_skirts_price_2)
a_line_skirts_1.add_child(a_line_skirts_design_1, a_line_skirts_color_1, a_line_skirts_price_1)
a_line_skirts_2.add_child(a_line_skirts_design_2, a_line_skirts_color_2, a_line_skirts_price_2)
bodycon_skirts_1.add_child(bodycon_skirts_design_1, bodycon_skirts_color_1, bodycon_skirts_price_1)
bodycon_skirts_2.add_child(bodycon_skirts_design_2, bodycon_skirts_color_2, bodycon_skirts_price_2)
mini_skirts_1.add_child(mini_skirts_design_1, mini_skirts_color_1, mini_skirts_price_1)
mini_skirts_2.add_child(mini_skirts_design_2, mini_skirts_color_2, mini_skirts_price_2)
jipsy_skirts_1.add_child(jipsy_skirts_design_1, jipsy_skirts_color_1, jipsy_skirts_price_1)
jipsy_skirts_2.add_child(jipsy_skirts_design_2, jipsy_skirts_color_2, jipsy_skirts_price_2)



# print(bags)
# print(dresses)
# print(footwear)
# print(accessories)
# print(tops)
# print(skirts)
# print(jeans_trousers)