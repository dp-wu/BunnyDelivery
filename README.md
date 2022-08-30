**Overview**
I worked on this smol JS browser game with a friend. The code is currently hosting on his GitHub, I want to remake it using pygame. It is a 2d platformer game with similar to trex-runner mechanism. It is a bunny continuously running dodging baddies to deliver taco/burrito/or whatever food the client orders.

**Gameplay Detail**
- Existing game:
  - Only one stage
  - Only two kinds of baddies: ducks, bunny jumps to dodge them; bird poops: not functioning properly at the moment due to unresolved collision issue, supposedly
damages bunny and lower HP (drop one heart) if not a “smack”;
  - Chankla will be delivered to bunny’s hand via tornado
  - Bunny can equip abuelita’s chankla to smack bird’s poop and shoot it towards duck
  - If there is a hit, the duck becomes harmless and screen shows “noice”
  - There is a current score on the top
  - There is a HP bar on the top but currently useless
- Pygame to be remake:
  - Create welcome scene for the game
  - Multiple stages (scenes) according to clients’ order (random)
  - Each scene should contain different map as well as different time interval - At least 3 kinds of baddies
  - Increase baddies’ moving speed as the bunny runs further
  - When a baddie gets hit, it flies away instead of becoming “harmless”
  - Functional HP bar
  - Better artworks
  - Store previous gameplay info in json file - Add animation for collisions
  - Autogenerate stage maps (scenes)

**Existing Problem**
- Shooting stars:
- The code is not reusable. I will need to remake the game completely and restructure everything with design pattern. Our game used CSS animation property A LOT. I eventually realized it’s a bad idea cuz it made adjusting objects with JS much harder (or maybe because both my friend and I were very bad at JS at the moment, we were scratching our heads trying to make the collision work, but it feels like the sprites have their own ideas and they just mind their own business).
- I think the other reason causing collision issue was the frame rate. The scenes might be updating too slow so then the collision is not being captured.
- The graphics are very ugly. I mean...  ̄\_(ツ)_/ ̄. I’m taking design101 class this semester from a local community college. Hopefully I’ll be able to make more acceptable graphics soon... ish?

**Timeline**
- Initialize the project and upload to Github — Aug 29 2022
- First iteration prototype — Sep 28 2022
- Second iteration — Oct 20 2022
