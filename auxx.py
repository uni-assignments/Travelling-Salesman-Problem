def instance_maker(): 

  df_cost = {'Twice Around The Tree': {}, 'Christofides': {}, 'Branch and Bound': {}}
  df_time = {'Twice Around The Tree': {}, 'Christofides': {}, 'Branch and Bound': {}}
  
  for i in range (4, 11):
    graph_euclidean = generate_graph('euclidean', 2**i)
    graph_manhattan = generate_graph('manhattan', 2**i)
    # show_graph(graph_euclidean)


    tat_e_t = time.time()
    tat_e_c = twice_around_the_tree(graph_euclidean) #twice around the tree euclidian cost - tat_e_c
    tat_e_t = time.time() - tat_e_t                  #twice around the tree manhattan time - tat_e_t

    tat_m_t = time.time()
    tat_m_c = twice_around_the_tree(graph_manhattan) #twice around the tree euclidian cost - tat_m_c
    tat_m_t = time.time() - tat_m_t                  #twice around the tree manhattan time - tat_m_t

    df_cost['Twice Around The Tree'][2**i] = ["{:.5f}".format(tat_e_c), "{:.5f}".format(tat_m_c)] 
    df_time['Twice Around The Tree'][2**i] = ["{:.5f}".format(tat_e_t), "{:.5f}".format(tat_m_t)] 

    print('\nTwice around the tree', 2**i, 'nodes:')
    print('Euclidean distance:', tat_e_c)
    print('Manhattan distance:', tat_m_c)

  for i in range (4, 11):
    graph_euclidean = generate_graph('euclidean', 2**i)
    graph_manhattan = generate_graph('manhattan', 2**i)
    # show_graph(graph_euclidean)

    # print('\nChristofides ', 2**i, 'nodes:')
    # print('Euclidean distance:', christofides (graph_euclidean))
    # print('Manhattan distance:', christofides(graph_manhattan))


  for i in range (4, 5):
    
    graph_euclidean = generate_graph('euclidean', 2**i)
    graph_manhattan = generate_graph('manhattan', 2**i)
    # show_graph(graph_euclidean)

    bab_e_t = time.time()
    bab_e_c = branch_and_bound(graph_euclidean)
    bab_e_t = time.time() - bab_e_t

    bab_m_t = time.time()
    bab_m_c = branch_and_bound(graph_manhattan)
    bab_m_t = time.time() - bab_m_t
    
    df_cost['Branch and Bound'][2**i] = ["{:.5f}".format(bab_e_c), "{:.5f}".format(bab_m_c)] 
    df_time['Branch and Bound'][2**i] = ["{:.5f}".format(bab_e_t), "{:.5f}".format(bab_m_t)] 

    print('\nBranch and Bound', 2**i, 'nodes:')
    print('Euclidean distance:', bab_e_c)
    print('Manhattan distance:', bab_m_c)


  pd.DataFrame(df_cost).to_csv('instance_costs.csv', index=True)
  pd.DataFrame(df_time).to_csv('instance_times.csv', index=True)


instance_maker()