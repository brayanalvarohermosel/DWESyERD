import sys
import matplotlib.pyplot as plt

def plot_points(points):
    jornadas = list(range(1, len(points) + 1))
    max_p = max(points)
    best_indices = [i for i, p in enumerate(points) if p == max_p]

    plt.figure(figsize=(8, 4.5))
    plt.plot(jornadas, points, marker='o', linestyle='-', color='tab:blue', label='Puntos')
    best_x = [i + 1 for i in best_indices]
    best_y = [max_p] * len(best_indices)
    plt.scatter(best_x, best_y, color='red', s=100, zorder=5, label='Mejor jornada')

    for x in best_x:
        plt.annotate(f'Mejor ({max_p})', xy=(x, max_p), xytext=(0, 8),
                     textcoords='offset points', ha='center', color='red', fontsize=9)

    plt.title('Puntos ganados por jornada')
    plt.xlabel('Jornada')
    plt.ylabel('Puntos')
    plt.xticks(jornadas)
    plt.grid(alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        try:
            points = [int(x) for x in sys.argv[1:]]
        except ValueError:
            sys.exit(1)
    else:
        points = [1, 3, 0, 2, 3, 3, 1, 0, 2, 3, 4]

    plot_points(points)