module solver
    use Rubic

    character(len=80), dimension(30) :: moves = &
             ["F  ", "Fi ", "Fw ", "Fiw", &
              "L  ", "Li ", "Lw ", "Liw", &
              "R  ", "Ri ", "Rw ", "Riw", &
              "U  ", "Ui ", "Uw ", "Uiw", &
              "D  ", "Di ", "Dw ", "Diw", &
              "B  ", "Bi ", "Bw ", "Biw", &
              "E  ", "Ei ", "rM ", "Mi ", &
              "S  ", "Si "]

    integer :: waitTime = 100
    integer :: moveCount = 0

    type::CommandLineInterface
        type(RubicCube) :: rc
        logical :: continue_ = .true.
    end type CommandLineInterface

    type::RubicSolver
        type(CommandLineInterface) :: ui
        type(RubicCube) :: rc
    end type RubicSolver


contains

    type(CommandLineInterface) function newCli()
        use rubic
        implicit none
        newCli%rc = newRC()
    end function
        

    type(RubicSolver) function newSolver(rc, ui)
        implicit none
        type(RubicCube) :: rc
        type(CommandLineInterface) :: ui
        newSolveR%rc = rc
        newSolver%ui = ui
    end function

    subroutine doCliThings(cli)
        implicit none
        type(CommandLineInterface) :: cli
        print *, "Hello! Welcome to Rushed Rubic's Cube!"
        do
            if (.not. cli%continue_) exit
            call display(cli)
            call chooseAction(cli)
        end do
    end subroutine

    subroutine display(cli)
        implicit none
        type(CommandLineInterface) :: cli
        call printStr(cli%rc)
    end subroutine

    subroutine chooseAction(cli)
        implicit none
        type(CommandLineInterface) :: cli
        character(len=1) :: choice
        print *, "Please choose what to d next."
        print *, "1. Randomize"
        print *, "2. Manual move"
        print *, "3. Explain possible moves"
        print *, "4. Solve the cube"
        print *, "5. Set move delay"
        print *, "6. Quit"
        print *, "Choice: "
        read(5, *) choice

        if (choice == "1") call cliRandomize(cli)
        if (choice == "2") call chooseMove(cli)
        if (choice == "3") call explainMoves()
        if (choice == "4") call cliSolve(cli)
        if (choice == "5") call setDelay(cli)
        if (choice == "6") cli%continue_ = .false.
        if (choice /= "1" .and. choice /= "2" &
        .and. choice /= "3" .and. choice /= "4" &
        .and. choice /= "5" .and. choice /= "6") &
          print *, "Please enter a valid number."
    end subroutine
    
    subroutine cliRandomize(cli)
        implicit none
        type(CommandLineInterface) :: cli
        integer :: moveCount, ios
        print *, "Please choose the number of random moves. Default 100: "
        read(5, *, iostat=ios) moveCount
        if (ios/=0) moveCount=100
        print *, "Randomizing.."
        call randomize(cli%rc, moveCount, .false.)
    end subroutine
    
    subroutine chooseMove(cli)
        implicit none
        type(CommandLineInterface) :: cli
        character(len=80) :: move
        print *, "Please choose a move"
        call listMoves()
        read(5, *) move
        call execute(cli%rc, move)
    end subroutine

    subroutine listMoves()
        implicit none
        print *, "Possible moves: "
        print *, moves
    end subroutine
    
    subroutine explainMoves()
        implicit none
        print *, "The cube has six faces."
        print *, "Front, left, right, up, down,  behind."
        print *, "We refer to these as F, L, R, U, D and B."
        print *, "It also has the following:"
        print *, "Middle, M - the layer between L and R."
        print *, "Equator, E - between U and D"
        print *, "Standing, S - betwen F and B"
        print *, ""
        print *, "Possible moves are as follows:"
        print *, "Rotate one of the faces, for instance F or L."
        print *, "By default, rotates a single layer clockwise."
        print *, "Suffix -i inverts the rotation."
        print *, "Suffix -w rotates two layers."
        print *, "When using both, i comes first. For instance, Uiw or Liw."
        print *, ""
        print *, "M, E and S can also be rotated."
        print *, "Rotation directions:"
        print *, "M: same as L, E: D and S: F"
        print *, ""
        print *, "Finally, the entire cube can be rotated around its x, y or z axis."
        print *, "x is like a hypotetical Rww rotation."
        print *, "y is like 'Uww', z is like 'Fww'."
    end subroutine
    
    subroutine cliSolve(cli)
        implicit none
        type(CommandLineInterface) :: cli
    end subroutine
    
    subroutine setDelay(cli)
        implicit none
        type(CommandLineInterface) :: cli
    end subroutine

    subroutine randomize(rc, moveCount, show)
        implicit none
        type(RubicCube) :: rc
        integer :: moveCount, i, ri
        logical :: show
        integer, parameter :: rk = selected_real_kind(4,20)
        real(kind=rk) :: r
        character(len=80) :: move
        do i=1,moveCount
            call random_number(r)
            ri = 1 + FLOOR(r*30_rk)
            move = moves(ri)
            if (show) then
                call uiDo(rc, move)
            else
                call execute(rc, move)
            end if
        end do
    end subroutine

    subroutine uiDo(rc, move)
        implicit none
        type(RubicCube) :: rc
        character(len=80) :: move
        integer :: i, j
        print *, "Executing move " // move
        call execute(rc, move)
        print *, "Current status:"
        call printStr(rc)
        do i=1, waitTime
            !Whose idea was to make sleep take
            !time as seconds in integers?!?
            j = i+1
            j = i-1
        end do
    end subroutine

    subroutine execute(rc, move)
        implicit none
        type(RubicCube) :: rc
        character(len=80) :: move
        select case (move)
        !And to think this was just a 
        !string to function map in python
        case ("F")
            call rF(rc)
        case ("Fi")
            call rFi(rc)
        case ("Fw")
            call rFw(rc)
        case ("Fiw")
            call rFiw(rc)
        case ("L")
            call rL(rc)
        case ("Li")
            call rLi(rc)
        case ("Lw")
            call rLw(rc)
        case ("Liw")
            call rLiw(rc)
        case ("R")
            call rR(rc)
        case ("Ri")
            call rRi(rc)
        case ("Rw")
            call rRw(rc)
        case ("Riw")
            call rRiw(rc)
        case ("U")
            call rU(rc)
        case ("Ui")
            call rUi(rc)
        case ("Uw")
            call rUw(rc)
        case ("Uiw")
            call rUiw(rc)
        case ("D")
            call rD(rc)
        case ("Di")
            call rDi(rc)
        case ("Dw")
            call rDw(rc)
        case ("Diw")
            call rDiw(rc)
        case ("B")
            call rB(rc)
        case ("Bi")
            call rBi(rc)
        case ("Bw")
            call rBw(rc)
        case ("Biw")
            call rBiw(rc)
        case ("E")
            call rE(rc)
        case ("Ei")
            call rEi(rc)
        case ("M")
            call rM(rc)
        case ("Mi")
            call rM(rc)
        case ("S")
            call rS(rc)
        case ("Si")
            call rSi(rc)
        case ("x")
            call x(rc)
        case ("y")
            call y(rc)
        case ("z")
            call z(rc)
        case ("xi")
            call xi(rc)
        case ("yi")
            call yi(rc)
        case ("zi")
            call zi(rc)
        end select
        moveCount = moveCount + 1
    end subroutine

end module solver

program RubicSolver
    use solver
    implicit none
    type(CommandLineInterface) :: cli
    cli = newCli()
    call doCliThings(cli)
end program RubicSolver
