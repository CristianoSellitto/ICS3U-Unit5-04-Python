#!/usr/bin/env python3

# Created by Cristiano Sellitto
# Created in December 2022
# A program that calculates a cylinder's volume

import math


def volume_of_a_cylinder(radius: int, height: int) -> float:
    # Calculates a cylinder's volume

    if radius < 0 or height < 0:
        return -1
    else:
        volume = math.pi * radius**2 * height
        return volume


def main():
    # Gets input and calls to calculate the volume of the cylinder

    print("\nThis program calculates a cylinder's volume.")
    print("V = πr²h")
    try:
        radius_text = input("\nEnter the cylinder's radius (mm): ")
        radius_integer = float(radius_text)
        height_text = input("Enter the cylinder's height (mm): ")
        height_integer = float(height_text)
        cylinder_volume = volume_of_a_cylinder(radius_integer, height_integer)
        print("\nThis cylinder's volume is {} mm³".format(cylinder_volume))
    except ValueError:
        print("\nYou did not enter a valid integer.")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
