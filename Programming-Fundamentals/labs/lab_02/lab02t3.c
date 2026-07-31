#include <stdio.h>
#include <math.h>

int main() {
    const float PI = 3.141592653;
    
    int a = 10, b = 5, c = 15, d = 20, theta = 45;
    float theta_rad = theta * PI / 180;
    
    float exp1 = pow((float) a / b * sin(theta_rad), a / pow(b, 2));
    float exp2 = pow((float) b / a * cos(theta_rad), 1.0 / (a + b));
    float exp3 = c * tan(theta_rad);
    float exp4 = (float) d / c;
    
    float exp_final = sqrt(exp1 + exp2) / (exp3 - exp4);
    
    printf("The answer is %f\n", exp_final);
    
    return 0;
}
