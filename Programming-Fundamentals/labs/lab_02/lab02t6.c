#include <stdio.h>

int main() {
    float download_speed, file_size, download_time;

    printf("Enter the download speed (in Mbps): ");
    scanf("%f", &download_speed);

    printf("Enter the file size (in MB): ");
    scanf("%f", &file_size);

    float file_size_in_Mb = file_size * 8;

    download_time = file_size_in_Mb / download_speed;

    printf("At %.2f, a file of %f MB downloads in %f seconds.\n", download_speed, file_size, download_time);
    
    return 0;
}
