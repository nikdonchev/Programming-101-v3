__author__ = 'Nikolay Donchev'
import fill_tetrahedron


def tetrahedron_filled(tetrahedrons, water):
    """
    This function takes two arguments: tetrahedrons and water.
    Then returns the maximum number of tetrahedrons filled with water we have.
    """
    sorted_tetrahedrons = sorted(tetrahedrons)
    print("Sorted list of tetrahedrons by length: {}".format(sorted_tetrahedrons))
    print("Amount of water: {} liters".format(water))
    total = 0
    filled_tetra = 0
    for idx, val in enumerate(sorted_tetrahedrons):
        print("Tetrahedron: {}   Length of a Regular tetrahedron: {}".format(idx + 1, val))
        total += fill_tetrahedron.fill_tetrahedron(val)
        if total >= water:
            filled_tetra = idx
        else:
            filled_tetra = idx + 1
    print()
    print("Amount of water needed for {} tetrahedrons {} liters".format(idx+1, total))
    print("We can fill {} tetrahedrons with {} liters of water".format(filled_tetra, water))

tetrahedron_filled([5, 15, 20], 10)
