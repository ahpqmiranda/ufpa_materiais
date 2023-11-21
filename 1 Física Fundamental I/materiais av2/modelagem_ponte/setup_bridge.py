import numpy as np
import pandas as pd
import sympy as sp
import anastruct as ana
import anastruct.fem.system as afs
import matplotlib.pyplot as plt

np.random.seed(19680801)
N = 50
colors = np.random.rand(N)
area = (30 * np.random.rand(N)) ** 2  # 0 to 15 point radii

# array format (x, y ,z)
base_d1 = np.array([[i * 115, 0, 0] for i in range(9)])
base_d2 = np.array([[i * 115, 115, 0] for i in range(9)])
sup_d1 = np.array([[(i + 1) * 115, 0, 115] for i in range(7)])
sup_d2 = np.array([[(i + 1) * 115, 115, 115] for i in range(7)])

group_nodes = [base_d1, base_d2, sup_d1, sup_d2]


def plot_nodes():
    fig = plt.figure(figsize=(25, 16), dpi=250)

    ax = fig.add_subplot(projection='3d')
    ax.set_xlim3d(-20, 1000)
    ax.set_ylim3d(-20, 120)
    ax.set_zlim3d(-20, 120)

    for i in group_nodes:
        for j in i:
            ax.scatter(xs=j[0], ys=j[1], zs=j[2], color='blue', marker='o', alpha=0.5, s=50)

    for i in group_nodes:
        for index, j in enumerate(i):
            if index + 1 < len(i):
                # print(index, j, i[index + 1])
                ax.plot(xs=[j[0], i[index + 1][0]],
                        ys=[j[1], i[index + 1][1]],
                        zs=[j[2], i[index + 1][2]],
                        color='blue')

    for id, i in enumerate(group_nodes):
        for index, j in enumerate(i):
            if len(group_nodes) > id + 1:
                a = len(group_nodes[id])
                b = len(group_nodes[id + 1])
                if a == b:
                    ax.plot(
                        xs=[j[0], group_nodes[id + 1][index][0]],
                        ys=[j[1], group_nodes[id + 1][index][1]],
                        zs=[j[2], group_nodes[id + 1][index][2]],
                        color='orange'
                    )

    for id, i in enumerate(group_nodes):
        for index, j in enumerate(i):
            a = len(group_nodes[id - 1])
            b = len(group_nodes[id])

            if a != b:
                # print(index, j, id, group_nodes[id + 1][index])
                ax.plot(
                    xs=[j[0], group_nodes[id + 1][index][0]],
                    ys=[j[1], group_nodes[id + 1][index][1]],
                    zs=[j[2], group_nodes[id + 1][index][2]],
                    color='orange'
                )

    list1 = base_d1.tolist()
    list2 = sup_d1.tolist()
    special_curve = list1[0], list2[0]
    ax.plot(xs=[special_curve[0][0], special_curve[1][0]],
            ys=[special_curve[0][1], special_curve[1][1]],
            zs=[special_curve[0][2], special_curve[1][2]],
            color='green'
            )
    special_curve = list1[-1], list2[-1]
    ax.plot(xs=[special_curve[0][0], special_curve[1][0]],
            ys=[special_curve[0][1], special_curve[1][1]],
            zs=[special_curve[0][2], special_curve[1][2]],
            color='green'
            )

    list1_trimmed = list1[1:-1]
    grouped_lists = list(zip(list1_trimmed, list2))

    for item in grouped_lists:
        ax.plot(xs=[item[0][0], item[1][0]],
                ys=[item[0][1], item[1][1]],
                zs=[item[0][2], item[1][2]],
                color='gray'
                )

    list1 = base_d2.tolist()
    list2 = sup_d2.tolist()
    special_curve = list1[0], list2[0]
    ax.plot(xs=[special_curve[0][0], special_curve[1][0]],
            ys=[special_curve[0][1], special_curve[1][1]],
            zs=[special_curve[0][2], special_curve[1][2]],
            color='green'
            )
    special_curve = list1[-1], list2[-1]
    ax.plot(xs=[special_curve[0][0], special_curve[1][0]],
            ys=[special_curve[0][1], special_curve[1][1]],
            zs=[special_curve[0][2], special_curve[1][2]],
            color='green'
            )

    list1_trimmed = list1[1:-1]
    grouped_lists = list(zip(list1_trimmed, list2))
    for item in grouped_lists:
        ax.plot(xs=[item[0][0], item[1][0]],
                ys=[item[0][1], item[1][1]],
                zs=[item[0][2], item[1][2]],
                color='gray'
                )

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    plt.show()

    return sup_d2


def test_combinations():
    list1 = base_d1.tolist()
    list2 = sup_d1.tolist()

    # Drop the first and last items from list1
    list1_trimmed = list1[1:-1]

    # Combine the trimmed list1 with list2

    # Group the combined list into sublists of length 2
    # [combined_list[i:i + 2] for i in range(0, len(combined_list), 2)]
    grouped_lists = list(zip(list1_trimmed, list2))

    for item in grouped_lists:
        print(item)


if __name__ == '__main__':
    plot_nodes()
