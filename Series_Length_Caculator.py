print("How to use:\nGive the amount of episodes of one length one by one.\nOnce you have given all the episodes for a series, press q to see the series' full length!\n")
while True:
    lengthSeries = [0,0,0]
    while True:
        lengthEpisodes = input("Give episode length (h:)m:s*episode_count, q to quit: ")  #esim 23:40*12  tai 1:20:00 *2

        if lengthEpisodes == "q":
            break
        lengthEpisodes = lengthEpisodes.split(":")        
        if len(lengthEpisodes) != 2 and len(lengthEpisodes) != 3:
            print("Input Error! Please give input again.")
            continue



        if len(lengthEpisodes) == 3:
            indexCorrection = 1
            hours = int(lengthEpisodes[0])
        else:
            indexCorrection = 0
            hours = 0

        try:
            multiplier = int(lengthEpisodes[1+indexCorrection].split("*")[1])
        except IndexError:
            multiplier = 1
        except ValueError:
            print("Give episode count only in numerals (123456789)! Please give input again.")
            continue
            

        try:
            seconds = int(lengthEpisodes[1+indexCorrection].split("*")[0])
            minutes = int(lengthEpisodes[0+indexCorrection])

            if minutes >60:
                print("Minutes are too large (>60)! Please give input again.")
                continue
            elif seconds >60:
                print("Seconds are too large (>60)! Please give input again.")
                continue
            elif minutes <0:
                print("Minutes are negative! Please give input again.")
                continue
            elif seconds <0:
                print("Seconds are negative! Please give input again.")
                continue
            elif hours <0:
                print("Seconds are negative! Please give input again.")
                continue


            lengthSeries[2] += seconds*multiplier
            lengthSeries[1] += minutes*multiplier
            lengthSeries[0] += hours*multiplier
        except ValueError:
            print("Give episode length only in numerals (123456789)! Please give input again.")


            


    lengthSeries[1] += int(lengthSeries[2] / 60 )
    lengthSeries[2] = lengthSeries[2] % 60
    lengthSeries[0] += int(lengthSeries[1] / 60)
    lengthSeries[1] = lengthSeries[1] % 60



    print(f"Series length is: {lengthSeries[0]}:{lengthSeries[1]}:{lengthSeries[2]}")

    if input("Do you want to close the program? y to quit: ") == "y":
        break