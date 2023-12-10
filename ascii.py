from termcolor import colored

def print_port_scanner_ascii():
    ascii_art = """                                                                                                                
 #   #          ##     #       #            ###   ####           ###                                            
 #   #           #     #                     #    #   #         #   #                                           
 ## ##  #   #    #    ####    ##             #    #   #         #       ###    ###   # ##   # ##    ###   # ##  
 # # #  #   #    #     #       #             #    ####           ###   #   #      #  ##  #  ##  #  #   #  ##  # 
 #   #  #   #    #     #       #             #    #                 #  #       ####  #   #  #   #  #####  #     
 #   #  #  ##    #     #  #    #             #    #             #   #  #   #  #   |  #   |  |   |  #      %
 #   #   ## #   ###     ##    ###           ###   #              ###    ###    ####  #   #  #   #   ###   #     
                                                                                                                
                                                                                                               """

    for char in ascii_art:
        color = 'red' if char == '#' else 'green' if char.isalpha() else 'white'
        print(colored(char, color), end='')

# Call the function to print the colored ASCII art
print_port_scanner_ascii()
