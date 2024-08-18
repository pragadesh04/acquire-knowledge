import pyautogui as pg
import time as t

t.sleep(5)

content = """import java.util.Scanner;

public class DiagonalSum {
public static void main(String[] args) {
Scanner scanner = new Scanner(System.in);
int[][] matrix = new int[10][10];
int sum = 0;

for (int i = 0; i < 10; i++) {
for (int j = 0; j < 10; j++) {
matrix[i][j] = scanner.nextInt();
if (i == j) {
sum += matrix[i][j];
}
}
}

System.out.println(sum);
}
}

"""

pg.typewrite(content, interval=0.01)