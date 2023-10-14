import AgentLists as Al

# Makes possible stores depending on user's level.

level_store = Al.all_agents  # practice store
level_1_store = Al.tier_1_agents                     # player level_1 store: tier (1)
level_2_store = level_1_store                        # player level 2 store: tier (1)
level_3_store = level_2_store + Al.tier_2_agents    # player level 3 store: tier (1, 2)
level_4_store = level_3_store + Al.tier_3_agents    # player level 4 store: tier (1, 2, 3)
level_5_store = level_4_store + Al.tier_4_agents    # player level 5 store: tier (1, 2, 3, 4)
level_6_store = level_5_store                       # player level 6 store: tier (1, 2, 3, 4)
level_7_store = level_6_store + Al.tier_5_agents    # player level 7 store: tier (1, 2, 4, 4, 5)
level_8_store = level_7_store                       # player level 8 store: tier (1, 2, 4, 4, 5)
level_9_store = level_8_store                       # player level 9 store: tier (1, 2, 4, 4, 5)

StoreAndLevel = {1: level_1_store, 2: level_2_store, 3: level_3_store, 4: level_4_store, 5: level_5_store,
                 6: level_6_store, 7: level_7_store, 8: level_8_store, 9: level_9_store}
