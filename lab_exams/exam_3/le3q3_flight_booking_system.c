#include <stdio.h>
#include <stdbool.h>
#include <string.h>

#define SEATS 100
#define SIZE 50

// forward declaration of Seat structure
typedef struct {
    int seatNum;
    char psnger[SIZE];
    bool bookStatus;
    float lugWght;
    char trvlCls[SIZE];
} Seat;

// flight structure
typedef struct {
    char name[SIZE];
    int departure;
    char dest[SIZE];
    int distance;
    int total_seats;
    Seat seatArr[SEATS];
} Flight;

// function to get luggage weight limit based on class
float getLuggageLimit(char *trvlCls) {
    if (strcmp(trvlCls, "Economy") == 0) {
        return 20.0;
    } else if (strcmp(trvlCls, "Business") == 0) {
        return 30.0;
    } else if (strcmp(trvlCls, "First") == 0) {
        return 40.0;
    }
    return 20.0; // Default
}

// function to get price per kilometer based on class
float getPricePerKm(char *trvlCls) {
    if (strcmp(trvlCls, "Economy") == 0) {
        return 0.5;
    } else if (strcmp(trvlCls, "Business") == 0) {
        return 0.8;
    } else if (strcmp(trvlCls, "First") == 0) {
        return 1.2;
    }
    return 0.5; // Default
}

// function to initialize all seats as unbooked
void initializeSeats(Flight *flight) {
    for (int i = 0; i < flight->total_seats; i++) {
        flight->seatArr[i].seatNum = i + 1;
        strcpy(flight->seatArr[i].psnger, "");
        flight->seatArr[i].bookStatus = false;
        flight->seatArr[i].lugWght = 0.0;
        strcpy(flight->seatArr[i].trvlCls, "");
    }
    printf("\nAll %d seats have been initialized as unbooked.\n", flight->total_seats);
}

// function to book a seat
void bookSeat(Flight *flight) {
    int seatNum;
    char passengerName[SIZE];
    float luggageWeight;
    char travelClass[SIZE];
    
    printf("\nBook a Seat\n");
    printf("Enter seat number (1-%d): ", flight->total_seats);
    scanf("%d", &seatNum);
    
    // Validate seat number
    if (seatNum < 1 || seatNum > flight->total_seats) {
        printf("Invalid seat number!\n");
        return;
    }
    
    // Check if seat is already booked
    if (flight->seatArr[seatNum - 1].bookStatus) {
        printf("Seat %d is already booked!\n", seatNum);
        return;
    }
    
    // get passenger details
    printf("Enter passenger name: ");
    scanf(" %[^\n]", passengerName);
    
    printf("Enter travel class (Economy/Business/First): ");
    scanf("%s", travelClass);
    
    printf("Enter luggage weight (kg): ");
    scanf("%f", &luggageWeight);
    
    // input all information and mark as booked
    flight->seatArr[seatNum - 1].seatNum = seatNum;
    strcpy(flight->seatArr[seatNum - 1].psnger, passengerName);
    strcpy(flight->seatArr[seatNum - 1].trvlCls, travelClass);
    flight->seatArr[seatNum - 1].lugWght = luggageWeight;
    flight->seatArr[seatNum - 1].bookStatus = true;
    
    // calculate ticket price
    float pricePerKm = getPricePerKm(travelClass);
    float basePrice = flight->distance * pricePerKm;
    
    float luggageLimit = getLuggageLimit(travelClass);
    float extraCharges = 0.0;
    
    if (luggageWeight > luggageLimit) {
        float excessWeight = luggageWeight - luggageLimit;
        extraCharges = excessWeight * 10.0; // $10 per kg
    }
    
    float totalPrice = basePrice + extraCharges;
    
    // display all the information once seat is booked
    printf("\nBooking Confirmed\n");
    printf("Seat Number: %d\n", seatNum);
    printf("Passenger Name: %s\n", passengerName);
    printf("Travel Class: %s\n", travelClass);
    printf("Luggage Weight: %.2f kg\n", luggageWeight);
    printf("Booking Status: BOOKED\n");
    
    printf("\nTicket Price Details\n");
    printf("Distance: %d km\n", flight->distance);
    printf("Base Price: $%.2f\n", basePrice);
    
    if (extraCharges > 0) {
        printf("Excess Luggage Charges: $%.2f (%.2f kg over limit)\n", 
               extraCharges, luggageWeight - luggageLimit);
    }
    
    printf("Total Price: $%.2f\n", totalPrice);
}

// function to display all booked seats
void displayBookedSeats(Flight *flight) {
    printf("\nAll Booked Seats\n");
    printf("Flight: %s\n", flight->name);
    printf("Destination: %s\n", flight->dest);
    printf("Distance: %d km\n\n", flight->distance);
    
    bool anyBooked = false;
    
    for (int i = 0; i < flight->total_seats; i++) {
        if (flight->seatArr[i].bookStatus) {
            anyBooked = true;
            printf("Seat %d:\n", flight->seatArr[i].seatNum);
            printf("  Passenger: %s\n", flight->seatArr[i].psnger);
            printf("  Class: %s\n", flight->seatArr[i].trvlCls);
            printf("  Luggage: %.2f kg\n", flight->seatArr[i].lugWght);
            printf("  Status: BOOKED\n\n");
        }
    }
    
    if (!anyBooked) {
        printf("No seats have been booked yet.\n");
    }
}

// function to initialize flight data
void initializeFlight(Flight *flight) {
    printf("Initialize Flight:\n");
    printf("Enter flight name: ");
    scanf(" %[^\n]", flight->name);
    
    printf("Enter departure time (24-hour format, e.g., 1430): ");
    scanf("%d", &flight->departure);
    
    printf("Enter destination: ");
    scanf(" %[^\n]", flight->dest);
    
    printf("Enter distance (km): ");
    scanf("%d", &flight->distance);
    
    printf("Enter total seats available (max %d): ", SEATS);
    scanf("%d", &flight->total_seats);
    
    if (flight->total_seats > SEATS) {
        flight->total_seats = SEATS;
        printf("Seats limited to maximum %d\n", SEATS);
    }
    
    // initialize all seats
    initializeSeats(flight);
}

int main() {
    Flight myFlight;
    int choice;
    
    // initialize flight data
    initializeFlight(&myFlight);
    
    // menu-driven program
    while (1) {
        printf("\nFlight Booking System:\n");
        printf("1. Book a Seat\n");
        printf("2. Display All Booked Seats\n");
        printf("3. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);
        
        switch (choice) {
            case 1:
                bookSeat(&myFlight);
                break;
            case 2:
                displayBookedSeats(&myFlight);
                break;
            case 3:
                printf("\nThank you for using the Flight Booking System!\n");
                return 0;
            default:
                printf("Invalid choice! Please try again.\n");
        }
    }
    
    return 0;
}
