/*  Copyright 2010 Curtis McEnroe <programble@gmail.com>
 *
 *  This file is part of programble-utils.
 *
 *  programble-utils is free software: you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation, either version 3 of the License, or
 *  (at your option) any later version.
 * 
 *  programble-utils is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with programble-utils.  If not, see <http://www.gnu.org/licenses/>.
 */

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[])
{
    if (argc >= 2)
    {
        if (strcmp(argv[1], "--help") == 0 || strcmp(argv[1], "-h") == 0)
        {
            printf("ed [ - ] [ -x ] [ name ]\n\n");
            printf("Ed is the standard text editor.\n");
            return 0;
        }
    }
    while (1)
    {
        char *input = NULL;
        size_t s;
        int success = getline(&input, &s, stdin);
        if (success == -1)
            return 1;
        if (success == 2 && input[0] == 'q')
            return 0;
        printf("?\n");
        free(input);
    }
}
