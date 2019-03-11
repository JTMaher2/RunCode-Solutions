#!/usr/bin/env python3

import sys
import math

def round(n):
    a = (n // 10) * 10

    b = a + 10

    return b

m_div_results = []

with open(sys.argv[1]) as input:
    for line in input:
        num = int(line)

        if num > 1:
            # round number up to nearest multiple of 10
            if num % 10 != 0:
                nearest_higher_mult_10 = round(num)
            else:
                nearest_higher_mult_10 = num

            # factor the number
            div_result = num
            while True:
                div_result = div_result / 2
                m_div_results.append(math.floor(div_result))
                if m_div_results[len(m_div_results) - 1] == 1:
                    break

            sys.stdout.write(str(nearest_higher_mult_10) + ' ')
            
            i = len(m_div_results) - 1

            nearest_higher_mult_10_plus_div_result = nearest_higher_mult_10 + m_div_results[i]

            sys.stdout.write(str(nearest_higher_mult_10_plus_div_result) + ' ')

            i -= 1

            while nearest_higher_mult_10_plus_div_result < (nearest_higher_mult_10 + 10):
                if i >= 0 and ((nearest_higher_mult_10_plus_div_result + m_div_results[i]) < (nearest_higher_mult_10 + 10)):
                    nearest_higher_mult_10_plus_div_result = nearest_higher_mult_10_plus_div_result + m_div_results[i]
                    sys.stdout.write(str(nearest_higher_mult_10_plus_div_result) + ' ')
                    i -= 1 # go to next div result
                elif (nearest_higher_mult_10_plus_div_result + m_div_results[0]) < (nearest_higher_mult_10 + 10):
                    # output highest div result
                    nearest_higher_mult_10_plus_div_result = nearest_higher_mult_10_plus_div_result + m_div_results[0]
                    sys.stdout.write(str(nearest_higher_mult_10_plus_div_result) + ' ')
                else:
                    # the highest num has been reached
                    sys.stdout.write(str(nearest_higher_mult_10_plus_div_result + num)) # finally, output result + input num
                    break