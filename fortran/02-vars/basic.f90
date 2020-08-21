program variables
    implicit none

    integer :: age
    real :: pi
    complex :: frequency
    character :: initial
    logical :: isOkay

    age = 28
    pi = 3.1415
    frequency = (1.0, -0.5)
    initial = 'F'
    isOkay = .true.

    print *, "Age is: ", age
    print *, "Pi is: ", pi
    print *, "Frequency is: ", frequency
    print *, "Initial is: ", initial
    print *, "Is okay? ", isOkay
    
end program variables