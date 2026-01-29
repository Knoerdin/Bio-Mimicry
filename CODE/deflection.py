import matplotlib.pyplot as plt
import numpy as np
import os

GRAVITY = 9.81
GRIPPER_MASS = 5.0

def calculate_deflection_pointmass(length, elasticity, thickness, diameter):
    i = (np.pi / 64) * (diameter**4 - (diameter - 2 * thickness)**4)
    deflection = (GRIPPER_MASS * GRAVITY * length**3) / (3 * elasticity * i)
    return deflection

def calculate_deflection_ownmass(density, length, elasticity, thickness, diameter):
    w = calculate_mass(diameter, length, thickness, density)[0]
    i = (np.pi / 64) * (diameter**4 - (diameter - 2 * thickness)**4)
    deflection = w * length**4 / (8 * elasticity * i)
    return deflection

def calculate_deflection(density, length, elasticity, thickness, diameter, material_name: str = None):
    mass = calculate_mass(diameter, length, thickness, density)[1]
    deflection = calculate_deflection_pointmass(length, elasticity, thickness, diameter) + calculate_deflection_ownmass(density, length, elasticity, thickness, diameter)
    deflection_dict = {
        "deflection": deflection,
        "material": material_name,
        "length": length,
        "weight": mass,
        "diameter": diameter,
        "thickness": thickness,
        "elasticity": elasticity,
    }
    return deflection_dict

def calculate_mass(diameter, length, thickness, density):
    inner_diameter = diameter - 2 * thickness
    outer_surface = np.pi * (diameter / 2)**2
    inner_surface = np.pi * (inner_diameter / 2)**2
    A = (outer_surface - inner_surface)
    w = A * density * GRAVITY
    mass = A * density * length
    return w, mass

def plot_deflection(deflections: list[dict]):
    # sort the deflections by deflection value (ascending) so the barplot
    # shows lowest deflection on the left and highest on the right
    sorted_deflections = sorted(deflections, key=lambda d: d['deflection'])

    thickness = [d['thickness'] for d in sorted_deflections]
    defl_values = [d['deflection'] for d in sorted_deflections]
    materials = [d['material'] for d in sorted_deflections]

    indices = np.arange(len(sorted_deflections))
    labels = [f"{m}\n{t:.3f} m" for m, t in zip(materials, thickness)]
    colors = plt.cm.tab10(indices / max(1, len(sorted_deflections) - 1))

    plt.figure(figsize=(10, 6))
    bars = plt.bar(indices, defl_values, color=colors)
    plt.xticks(indices, labels)

    for bar, val in zip(bars, defl_values):
        h = bar.get_height()
        plt.annotate(f"{val:.4e}", xy=(bar.get_x() + bar.get_width() / 2, h),
                     xytext=(0, 4), textcoords="offset points", ha='center', va='bottom', fontsize=8)

    plt.title('Beam Deflection by Material / Thickness')
    plt.xlabel('Material (thickness)')
    plt.ylabel('Deflection (m)')

    legend_labels = [
        f"{d['material']}: L={d['length']}m, D={d['diameter']}m, E={d['elasticity']/1e9}GPa, W={d['weight']:.2f}kg"
        for d in sorted_deflections
    ]
    plt.legend(bars, legend_labels, loc='upper left', bbox_to_anchor=(1, 1))
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

def main():
    go_on = True
    deflections = []
    while go_on:

        material_name = input('Enter the material name: ')
        length = float(input('Enter the length of the beam (in meters): '))
        diameter = float(input('Enter the diameter of the beam (in cm): '))/100
        thickness = float(input('Enter the thickness of the beam (in mm): '))/1000
        elasticity = float(input('Enter the modulus of elasticity (in Pascals): '))*1000000000
        density = float(input('Enter the density of the material (in kg/m^3): '))
        result = calculate_deflection(float(density), float(length), float(elasticity), float(thickness), float(diameter), material_name)
        print(f"The calculated deflection is: {result['deflection']} meters")

        # add the dict to a text file for future reference
        with open('deflection_results.txt', 'a') as f:
            # if the entry already exists, skip it
            if str(result) + '\n' not in open('deflection_results.txt').read():
                f.write(str(result) + '\n')
        go_on = input('Do you want to calculate another deflection? (yes/no): ').lower() == 'yes'
    print(deflections)
    # open the text file and use the stored dicts to plot a bar chart
    if os.path.exists('deflection_results.txt'):
        with open('deflection_results.txt', 'r') as f:
            lines = f.readlines()
            for line in lines:
                deflections.append(eval(line.strip()))
        plot_deflection(deflections)
    else:
        print("No deflection results found to plot.")

if __name__ == "__main__":
    main()