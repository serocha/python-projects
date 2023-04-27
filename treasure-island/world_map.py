from Location import Location
from Exit import Exit

crossroads = Location(
  "crossroads",
  'You are at a crossroads. You see a lake to your left, and a jagged cliff to your right.',
  exits=[
    Exit('left', "lake", "You make your way down the trail toward the lake, taking note of the unnaturally-calm water."),
    Exit('right', "cliff", "You head up the trail towards the imposing rockface.")
  ]
)

lake = Location(
  "lake",
  "You're standing at the edge of a dark, murky lake with no way to see what's beneath the glassy surface. There is an island in the middle of the lake, some way off. A rickety boat lies beached nearby.",
  exits=[
    Exit('boat', "island shore", "You hop onto the wooden boat and start rowing towards the island. The dark shapes of dozens of small creatures skim just beneath the surface of the water."), 
    Exit('go back', "crossroads", "You hike back towards the crossroads."), 
    Exit('swim', None, None, None, "As you plunge into the filthy water, you realize too late that it's infested with flesh-eating leeches. Within moments, they swarm you and drag you down to the depths...")
  ]
)

cliff = Location(
  "cliff",
  "You're standing at the base of a steep and treacherous cliff, with jagged rocks jutting out from its face. There's a small, dark cave at the base.",
  exits=[
    Exit('climb', 'clifftop', "With your rope and pitons, you slowly and steadily make your way up the cliff, carefully testing each hold before trusting your weight to it.", "climbing gear", "You begin to climb the cliff with your bare hands. It leaves you breathless, but the top finally comes within reach. You grab the edge only for the loose rock to crumble in your hand, sending you plummeting to the ground below..."), 
    Exit('go back', "crossroads", "You walk down from the cliffside back to the crossroads."), 
    Exit('cave', "cave", "Hesitantly, you step into the darkness of the cave, your feet crunching loudly on something.")
  ]
)

cave = Location(
  "cave",
  "The cave is dark and musty, and as your eyes adjust, you can make out a grim sight: the floor is littered with the bones of some unlucky souls who came before you.",
  'climbing gear',
  "One of the skeletons catches your eye: it wears a mostly-intact backpack. Inside you find a rope and some pitons.",
  [Exit('go back', 'cliff', "You leave the cave in a hurry, not wishing to linger.")]
)

clifftop = Location(
  "clifftop",
  "You finally reach the top of the cliff and find yourself standing on a narrow clifftop where a scraggly apple tree is growing. You have a breathtaking view of the surrounding landscape. In the middle of the lake you saw earlier is a small island, upon which stands a crumbling ruin.",
  'apple',
  "You pluck an apple from the tree and place it into your haversack.",
  [Exit('climb down', 'cliff', "You carefully loop the rope around a sturdy rock formation and begin inching your way back down to solid ground.")]
)

island_shore = Location(
  "island shore",
  "Standing upon the shore of the island, your boots sink deeply into the mud. The air is thick with the smell of decaying vegetation. A thin trail leads into the forest. Your boat lies beached, soon to be another rotting hulk: it surely would sink if you tried a return trip.",
  exits=[
    Exit('trail', "glade", "You follow the trail into the dense forest, the only sounds the rustle of leaves underfoot and the distant call of a bird in the treetops above."),
    Exit('shoreline', "shack", "You follow the shoreline, the still waters of the lake gently lapping against the rocks. Your feet crunch on the discarded shells of long dead mollusks.")
  ]
)

    # A battered rowboat is beached nearby, its paint peeling and its oars lying haphazardly on the ground.
shack = Location(
  "shack",
  "As you stand outside the dilapidated shack, you notice that the door is slightly ajar. It swings back and forth on rusty hinges, creaking as the lake breeze pushes it open and closed. A dense woodline lays to the west. You see where you landed back down the shore.",
  exits=[
    Exit('to boat', "island shore", "You make the trek back to the landing, the scent of brackish water growing stronger."),
    Exit('woods', "glade", "Leaving the dilapidated hut behind, you make your way into the woods, dead trees casting dappled shadows."),
    Exit('enter shack', "shack interior", "You cautiously approach the partially-open door of the dilapidated shack.")
  ]
)

glade = Location(
  "glade",
  "The trail passes through a small glade where the gnarled branches of the undergrowth seem to point skyward. In the middle stands a twisted tree with no leaves and a single fruit hanging from a bulbous bough. South lies your ruined boat. To the east, you spot a shack along the shore. The trail continues north into the forest.",
  exits=[
    Exit('south', "island shore", "You walk back along the trail until the underbrush slowly clears, revealing the rotten boat beached along the shore."),
    Exit('east', "shack", "You head east, the stillness of the forest giving way to the sound water softly lapping at the shore."),
    Exit('north', "end", "You push north into the woods. The trees form an oppressive canopy, and you feel a cold draft."),
    Exit('take fruit', "tree", "You approach the tree, stepping carefully over thick, contorted roots.")
  ]
)

end = Location(
    "end",
    """
    .....                                          ..      .                      ..       
 .H8888888h.  ~-.    .uef^"                     x88f` `..x88. .>                dF         
 888888888888x  `> :d88E                      :8888   xf`*8888%     u.    u.   '88bu.      
X~     `?888888hx~ `888E            .u       :8888f .888  `"`     x@88k u@88c. '*88888bu   
'      x8.^"*88*"   888E .z8k    ud8888.     88888' X8888. >"8x  ^"8888""8888"   ^"*8888N  
 `-:- X8888x        888E~?888L :888'8888.    88888  ?88888< 888>   8888  888R   beWE "888L 
      488888>       888E  888E d888 '88%"    88888   "88888 "8%    8888  888R   888E  888E 
    .. `"88*        888E  888E 8888.+"       88888 '  `8888>       8888  888R   888E  888E 
  x88888nX"      .  888E  888E 8888L         `8888> %  X88!        8888  888R   888E  888F 
 !"*8888888n..  :   888E  888E '8888c. .+     `888X  `~""`   :    "*88*" 8888" .888N..888  
'    "*88888888*   m888N= 888>  "88888%         "88k.      .~       ""   'Y"    `"888*""   
        ^"***"`     `Y"   888     "YP'            `""*==~~`                        ""      
                         J88"                                                              
                         @%                                                                
                       :"                                                                        
You've reached the end of the current content! Thanks for playing!
Type quit to go back to the main menu.
"""
)

map = [crossroads, lake, cliff, cave, clifftop, island_shore, shack, glade, end]