#include <math.h>
#include <cs50.h>
#include <stdio.h>
int main(void)
{
    int long long  card;
    int long long a_mod, b_mod, c_mod, d_mod, e_mod, f_mod, g_mod, h_mod, i_mod, j_mod, k_mod, l_mod, m_mod, n_mod, o_mod, p_mod;
    int a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t;

    card = get_long("Number: "); //Request data from the user

    a = (card / 1000000000000000) * 2;  // paired number

    // Run the "Luhn’s Algorithm" check.

    if (a > 9) // Multiply all the paired digits from the entered number by 2 and check if they are more than 9
    {
        a = (a / 10) + (a % 10); //if the number is greater than 9, that is, 10, 11, 12 ..., divide it into separate numbers
    }
    a_mod = card % 1000000000000000; //remove the first digit from the entered number, to reduce its multiplicity, to calculate the next digit in the number

    b = a_mod / 100000000000000; // unpaired number
    b_mod = a_mod % 100000000000000;

    c = (b_mod / 10000000000000) * 2; // paired number
    if (c > 9)
    {
        c = (c / 10) + (c % 10);
    }
    c_mod = b_mod % 10000000000000;

    d = c_mod / 1000000000000; // unpaired number
    d_mod = c_mod % 1000000000000;

    e = (d_mod / 100000000000) * 2; // paired number
    if (e > 9)
    {
        e = (e / 10) + (e % 10);
    }
    e_mod = d_mod % 100000000000;

    f = e_mod / 10000000000; // unpaired number
    f_mod = e_mod % 10000000000;

    g = (f_mod / 1000000000) * 2; // paired number
    if (g > 9)
    {
        g = (g / 10) + (g % 10);
    }
    g_mod = f_mod % 1000000000;

    h = g_mod / 100000000; // unpaired number
    h_mod = g_mod % 100000000;

    i = (h_mod / 10000000) * 2; // paired number
    if (i > 9)
    {
        i = (i / 10) + (i % 10);
    }
    i_mod = h_mod % 10000000;

    j = i_mod / 1000000; // unpaired number
    j_mod = i_mod % 1000000;

    k = (j_mod / 100000) *2; // paired number
    if (k > 9)
    {
       k = (k / 10) + (k % 10);
    }
    k_mod = j_mod % 100000;

    l = k_mod / 10000; // unpaired number
    l_mod = k_mod % 10000;

    m = (l_mod / 1000) * 2; // paired number
    if (m > 9)
    {
        m = (m / 10) + (m % 10);
    }
    m_mod = l_mod % 1000;

    n = m_mod / 100; // unpaired number
    n_mod = m_mod % 100;

    o = (n_mod / 10) * 2; // last paired number
    if (o > 9)
    {
        o = (o / 10) + (o % 10);
    }
    o_mod = n_mod % 10;

    p = o_mod % 10; // last unpaired number

    q = o + m + k + i + g + e + c + a; //Calculating the sum of paired numbers
    r = p + n + l + j + h + f + d + b; //Calculating the sum of unpaired numbers
    s = q + r; //Calculating the sum of paired and unpaired numbers

    if (s % 10 == 0) // If s% 10 = 0, then "Luhn’s Algorithm" works!
        // Start checking for map types
        {
            //American Express uses 15-digit numbers. All American Express numbers start with 34 or 37.
            if (card >=340000000000000 && card <350000000000000)
            {
                printf("AMEX\n");
            }

            else if(card >=370000000000000 && card <380000000000000) //
                {
                    printf("AMEX\n");
                }

                //MasterCard uses 16-digit numbers. Start with 51, 52, 53, 54, or 55.
                else if(card >=5100000000000000 && card <5600000000000000)
                {
                    printf("MASTERCARD\n");
             }

            //Visa uses 13- and 16-digit numbers. Visa numbers start with 4.
            else if(card >=4000000000000 && card <5000000000000)
            {
                printf("VISA\n");
            }
            else if(card >=4000000000000000 && card <5000000000000000)
            {
                printf("VISA\n");
            }
            else
            {
                printf("INVALID\n");
            }
        }
        else //If (s % 10) > 0, then "Luhn’s Algorithm" does not work!
        {
             printf("INVALID\n"); // Display INVALID
        }
}
