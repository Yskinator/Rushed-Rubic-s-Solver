module solver
    use Rubic

    character(len=80), dimension(30) :: moves = &
             ["F  ", "Fi ", "Fw ", "Fiw", &
              "L  ", "Li ", "Lw ", "Liw", &
              "R  ", "Ri ", "Rw ", "Riw", &
              "U  ", "Ui ", "Uw ", "Uiw", &
              "D  ", "Di ", "Dw ", "Diw", &
              "B  ", "Bi ", "Bw ", "Biw", &
              "E  ", "Ei ", "M  ", "Mi ", &
              "S  ", "Si "]

    logical :: waitTime = .false.
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
        if (choice == "5") call setDelay()
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
        write(6,'(A)'), moves
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
        moveCount=0
        call solve(cli%rc,cli)
        print *, "Total moves", moveCount
    end subroutine

    subroutine solve(rc, ui)
        implicit none
        type(RubicCube) :: rc
        type(CommandLineInterface) :: ui
        print *, "Priming cube."
        call primeCube(rc, ui)
        print *, "Primed."
        print *, "Phase 1."
        call printStr(rc)
        call phase1(rc,ui)
        print *, "Phase 1 completed."
        print *, "Phase 2."
        call printStr(rc)
        call phase2(rc,ui)
        print *, "Phase 2 completed."
        print *, "Phase 3."
        call printStr(rc)
        call phase3(rc,ui)
        print *, "Phase 3 completed."
        print *, "Phase 4."
        call printStr(rc)
        call phase4(rc, ui)
        print *, "Phase 4 completed."
        print *, "Phase 5."
        call printStr(rc)
        call phase5(rc,ui)
        print *, "Phase 5 completed."
        print *, "Phase 6."
        call printStr(rc)
        call phase6(rc,ui)
        print *, "Phase 6 completed."
        print *, "Phase 7."
        call printStr(rc)
        call phase7(rc,ui)
        print *, "Phase 7 completed. Cube solved!"
        ui%continue_ = .false.
    end subroutine

    subroutine phase7(rc, ui)
        implicit none
        type(RubicCube) :: rc
        type(CommandLineInterface) :: ui
        integer :: i, pattern
        character(len=80) :: move
        move = "y"
        do i=1,4
           pattern = findPattern(rc,ui)
           if (pattern==1) call p7a1(rc,ui)
           if (pattern==2) call p7a2(rc,ui)
           call uiDo(rc, move)
        end do
    end subroutine


    integer function findPattern(rc, ui)
        implicit none
        type(RubicCube) :: rc
        type(CommandLineInterface) :: ui
        character(len=1) :: UColor
        UColor = rc%U(2,2)
        if ((rc%U(1,2) /= UColor) .and. &
            (rc%U(3,2) /= UColor)) then
            findPattern=1
            return
        end if
        if ((rc%U(3,2) /= UColor) .and. &
            (rc%U(2,3) /= UColor)) then
            findPattern=2
            return
        end if
    end function

    subroutine phase6(rc, ui)
        implicit none
        type(RubicCube) :: rc
        type(CommandLineInterface) :: ui
        integer :: i
        character(len=80) :: move
        character(len=1) :: FColor
        logical :: found
        found = .false.
        do
            if (found) exit
            do i=1,4
                FColor = rc%F(2,2)
                if ((rc%F(2,1) == FColor) .or. &
                    (rc%U(2,3) == FColor)) then
                    found = .true.
                    exit
                else
                    move = "y"
                    call uiDo(rc,move)
                end if
            end do
            if (.not. found) call p6a1(rc,ui)
        end do
        do
            if (phase6Done(rc,ui)) exit
            call p6a1(rc,ui)
        end do
    end subroutine


    logical function phase6Done(rc, ui)
        implicit none
        type(RubicCube) :: rc
        type(CommandLineInterface) :: ui
        character(len=1) LColor, RColor, BColor
        LColor = rc%L(2,2)
        RColor = rc%R(2,2)
        BColor = rc%B(2,2)
        phase6Done = &
         (((rc%R(2,1) == Rcolor) .or. &
           (rc%U(3,2) == RColor)) .and. &
          ((rc%L(2,1) == LColor) .or. &
           (rc%U(1,2) == LColor)) .and. &
          ((rc%B(2,3) == BColor) .or. &
           (rc%U(2,1) == BColor)))
    end function 

    subroutine phase5(rc, ui)
        implicit none
        type(RubicCube) :: rc
        type(CommandLineInterface) :: ui
        integer :: i, pos
        character(len=80) :: move
        logical :: moved
        do
            if (phase5Done(rc,ui)) exit
            moved = .false.
            do i=1,4
                if (hasPattern(rc,ui)) then
                    call p5a1(rc,ui)
                    moved = .true.
                    exit
                end if
                move = "y"
                call uiDo(rc,move)
            end do
            if (.not. moved) call p5a1(rc,ui)
        end do
    end subroutine

    logical function hasPattern(rc,ui)
        implicit none
        type(RubicCube) :: rc
        type(CommandLineInterface) :: ui
        character(len=1) :: UColor
        UColor = rc%U(2,2)
        hasPattern = &
         (((rc%F(1,1) == UColor) .and. &
          (rc%U(3,3) == UColor)) .or. &
         ((rc%R(1,1) == UColor) .and. &
          (rc%R(3,1) == UColor)) .or. &
         ((rc%U(3,3) == UColor) .and. &
          (rc%R(3,1) == UColor)))
    end function

    logical function phase5Done(rc,ui)
        implicit none
        type(RubicCube) :: rc
        type(CommandLineInterface) :: ui
        character(len=1) :: UColor
        UColor = rc%U(2,2)
        phase5Done = &
         ((rc%U(1,1) == UColor) .and. &
          (rc%U(3,1) == UColor) .and. &
          (rc%U(3,3) == UColor) .and. &
          (rc%U(1,3) == UColor))
    end function

    subroutine phase4(rc, ui)
        implicit none
        type(RubicCube) :: rc
        type(CommandLineInterface) :: ui
        integer :: i, pos
        character(len=80) :: move
        move = "x"
        call uiDo(rc, move)
        call uiDo(rc, move)
        do i=1,2
            pos = whichToSwitch(rc, ui)
            if ((pos==5) .or. (pos==6)) then
                move = "y"
                call uiDo(rc,move)
                call p4a1(rc,ui)
                move = "yi"
                call uiDo(rc,move)
            end if
            if ((pos==1) .or. (pos==5)) then
                call p4a1(rc,ui)
            end if
            if ((pos==2) .or. (pos==6)) then
                call p4a2(rc,ui)
            end if
            if (pos==3) then
                call p4a1(rc,ui)
                call p4a2(rc,ui)
            end if
            move = "y"
            call uiDo(rc,move)
        end do
    end subroutine

    integer function whichToSwitch(rc, ui)
        implicit none
        type(RubicCube) :: rc
        type(CommandLineInterface) :: ui
        integer :: s24, s12, s34
        character(len=1) :: LColor
        LColor = rc%L(2,2)
        s24 = 0
        s12 = 0
        s34 = 0
        if ((rc%L(3,1) /= LColor) .and. &
           (rc%F(1,1) /= LColor) .and. &
           (rc%U(1,3) /= LColor)) then 
            s12 = 1
        end if
        if ((rc%L(1,1) /= LColor) .and. &
           (rc%B(1,3) /= LColor) .and. &
           (rc%U(1,1) /= LColor)) then 
            s34 = 2
        end if
        if ((s12 == 1) .and.  &
           (rc%R(1,1) /= LColor) .and. &
           (rc%F(3,1) /= LColor) .and. &
           (rc%U(3,3) /= LColor)) then 
            s24 = 4
        end if
        if ((s34 == 2) .and. &
           (rc%R(3,1) /= LColor) .and. &
           (rc%B(3,3) /= LColor) .and. &
           (rc%U(3,1) /= LColor)) then 
            s24 = 4
        end if
        whichToSwitch=(s12 + s34 + s24)
    end function

    subroutine phase2(rc, ui)
        implicit none
        type(RubicCube) :: rc
        type(CommandLineInterface) :: ui
        integer :: sidesFound, pos
        character(len=80) :: move
        sidesFound=0
        do
          if (sidesFound == 4) return
          pos = LookForUSide(rc,ui)
          if (pos==0) then
              if (checkIfP2Complete(rc)) then
                  return
              end if
          end if
          if (pos==1) then
             call p2a1(rc,ui)
             sidesFound = sidesFound+1
          end if
          if (pos==2) then
             call p2a2(rc,ui)
             sidesFound = sidesFound+1
          end if
          if (pos==3) then
             call p2a3(rc,ui)
             sidesFound = sidesFound+1
          end if
          if (pos==4) then
             call p2a4(rc,ui)
             sidesFound = sidesFound+1
          end if
          if (pos==5) then
             call p2a5(rc,ui)
             sidesFound = sidesFound+1
          end if
          if (pos==6) then
             call p2a1(rc,ui)
             sidesFound = sidesFound+1
          end if
          move = "y"
          call uiDo(rc,move)
        end do
    end subroutine

    subroutine phase3(rc, ui)
        implicit none
        type(RubicCube) :: rc
        type(CommandLineInterface) :: ui
        integer :: sidesFound, pos
        character(len=80) :: move
        sidesFound=0
        call rotateMiddle(rc, ui)
        do
            if (sidesFound == 4) return
            pos = findMiddleLayerEdge(rc,ui)
            if (pos == 0) then
                return
            end if
            if (pos == 1) then
                call p3a1(rc,ui)
                sidesFound = sidesFound+1
            end if
            if (pos == 2) then
                call p3a2(rc,ui)
                sidesFound = sidesFound+1
            end if
            if (pos == 3) then
                call p3a1(rc,ui)
            end if
            if (pos == 4) then
                call p3a2(rc,ui)
            end if
        end do
    end subroutine

    integer function findMiddleLayerEdge(rc, ui)
        implicit none
        type(RubicCube) :: rc
        type(CommandLineInterface) :: ui
        integer :: i,j
        character(len=80) :: move
        character(len=1) :: FColor, LColor, RColor
        do i=1,4
            move = "y"
            call uiDo(rc,move)
            FColor = rc%F(1,1)
            LColor = rc%L(1,1)
            RColor = rc%R(1,1)
            do j=1,4
                if (rc%F(2,3) == FColor) then
                    if (rc%D(2,1) == LColor) then
                        findMiddleLayerEdge=1
                        return
                    end if
                    if (rc%D(2,1) == RColor) then
                        findMiddleLayerEdge=2
                        return
                    end if
                end if
                if ((rc%F(1,2) == LColor) .and. (rc%L(3,2) == FColor)) then
                    findMiddleLayerEdge=3
                    return
                end if
                if ((rc%F(3,2) == RColor) .and. (rc%R(1,2) == FColor)) then
                    findMiddleLayerEdge=4
                    return
                end if
                move = "D"
                call uiDo(rc,move)
            end do
        end do
    end function

    subroutine rotateMiddle(rc, ui)
        implicit none
        type(RubicCube) :: rc
        type(CommandLineInterface) :: ui
        character(len=1) :: FColor
        character(len=80) :: move
        integer :: i
        FColor = rc%F(1,1)
        do i=1,4
            if (rc%F(2,2) == FColor) return
            move = "E"
            call uiDo(rc,move)
        end do
    end subroutine

    logical function checkIfP2Complete(rc)
        implicit none
        type(RubicCube) :: rc
        checkIfP2Complete = &
        ((rc%U(2,1) == rc%U(3,2)) .and. &
        (rc%U(3,2) == rc%U(2,3)) .and. &
        (rc%U(2,3) == rc%U(1,2)))
    end function

    integer function lookForUSide(rc,ui)
        implicit none
        type(RubicCube) :: rc
        type(CommandLineInterface) :: ui
        character(len=1) :: UColor, FColor
        character(len=80) :: move
        integer :: i
        UColor = rc%U(2,2)
        FColor = rc%F(1,1)
        do i=1, 4
            if ((rc%U(2,3) == UColor) .and. &
               (rc%F(2,1) == FColor)) then
                lookForUSide=0
                return
            end if
            if ((rc%D(2,1) == UColor) .and. &
                 (rc%F(2,3) == FColor)) then
                lookForUSide=1
                return
            end if
            if ((rc%F(2,3) == UColor) .and. &
                 (rc%D(2,1) == FColor)) then
                lookForUSide=2
                return
            end if
            if ((rc%R(1,2) == UColor) .and. &
                 (rc%F(3,2) == FColor)) then
                lookForUSide=3
                return
            end if
            if ((rc%F(3,2) == UColor) .and. &
                 (rc%R(1,2) == FColor)) then
                lookForUSide=4
                return
            end if
            if ((rc%F(2,1) == UColor) .and. &
                 (rc%U(2,3) == FColor)) then
                lookForUSide=5
                return
            end if
            move = "Dw"
            call uiDo(rc,move)
        end do
        do i=1,4
            move = "y"
            call uiDo(rc,move)
            if (((rc%U(2,3) == UColor) .and. &
               (rc%F(2,1) == FColor)) .or. &
               ((rc%F(2,1) == UColor) .and. &
               (rc%U(2,3) == FColor))) then
                lookForUSide=6
                return
             end if
        end do
        lookForUSide=-1
        return 
    end function


    subroutine phase1(rc, ui)
        implicit none
        type(RubicCube) :: rc
        type(CommandLineInterface) :: ui
        integer :: cornersFound, pos
        character(len=80) :: move
        cornersFound = 1
        do
            if (cornersFound >=4) exit
            move = "y"
            call uiDo(rc, move)
            pos = lookForUCorner(rc,ui)
            if (pos==0) cornersFound = cornersFound+1
            if (pos==1) then
                call p1a1(rc,ui)
                cornersFound = cornersFound+1
            end if
            if (pos==2) then
                call p1a2(rc,ui)
                cornersFound = cornersFound+1
            end if
            if (pos==3) then
                call p1a3(rc,ui)
                cornersFound = cornersFound+1
            end if
            if (pos==4) then
                call p1a4(rc,ui)
                cornersFound = cornersFound+1
            end if
            if (pos==5) then
                call p1a5(rc,ui)
                cornersFound = cornersFound+1
            end if
            if (pos==-1) then
                if (cornersFound == 1) then
                    move = "y"
                    call uiDo(rc, move)
                    call p1a1(rc,ui)
                    call uiDo(rc,move)
                    call p1a1(rc, ui)
                    move = "yi"
                    call uiDo(rc,move)
                    call uiDo(rc,move)
                    call uiDo(rc,move)
                else
                    if (cornersFound == 2) then
                        move = "y"
                        call uiDo(rc, move)
                        call p1a1(rc,ui)
                        move = "yi"
                        call uiDo(rc,move)
                        call uiDo(rc,move)
                    end if
                end if
            end if
        end do
    end subroutine

    integer function lookForUCorner(rc,ui)
        implicit none
        type(RubicCube) :: rc
        type(CommandLineInterface) :: ui
        character(len=80) :: move
        character(len=1) :: UColor, FColor
        integer :: lookCount
        UColor = rc%U(2,2)
        FColor = rc%F(1,1)
        do lookCount=1,4
            if ((rc%U(3,3) == UColor) .and. &
               (rc%F(3,1) == FColor)) then
                lookForUCorner=0
                return
            end if
            if ((rc%R(1,3) == UColor) .and. &
               ((rc%F(3,3) == FColor) .or. &
                 (rc%D(3,1) == FColor))) then
                lookForUCorner=1
                return
            end if
            if ((rc%F(3,3) == UColor) .and. &
               ((rc%D(3,1) == FColor) .or. &
                (rc%R(1,3) == FColor))) then
                lookForUCorner=2
                return
            end if
            if ((rc%D(3,1) == UColor) .and. &
               ((rc%R(1,3) == FColor .or. &
                 rc%F(3,3) == FColor))) then
                lookForUCorner=3
                return
            end if
            if ((rc%F(3,1) == UColor) .and. &
                ((rc%U(3,3) == FColor) .or. &
                 (rc%R(1,1) == FColor))) then
                lookForUCorner=4
                return
            end if
            if ((rc%R(1,1) == UColor) .and. &
                 ((rc%U(3,3) == FColor) .or. &
                 (rc%F(3,1) == FColor))) then
                lookForUCorner=5
                return
            end if
            move = "D"
            call uiDo(rc,move)
        end do
        lookForUCorner=-1
        return
    end function

    recursive subroutine primeCube(rc, ui)
        implicit none
        type(RubicCube) :: rc
        type(CommandLineInterface) :: ui
        if (UCorner(rc, ui)) return
        if (FCorner(rc,ui)) return
        if (LCorner(rc, ui)) return
        if (RCorner(rc,ui)) return
        if (BCorner(rc,ui)) return
        if (DCorner(rc,ui)) return
        call randomize(rc, 10, .true.)
        call primeCube(rc, ui)
    end subroutine

    logical function UCorner(rc, ui)
        implicit none
        type(RubicCube) :: rc
        type(CommandLineInterface) :: ui
        character(len=1) :: color
        character(len=80) :: move
        color = rc%U(2,2)
        if (rc%U(3,3) == color) then
            UCorner = .true.
            return
        end if
        if (rc%U(1,3) == color) then
            move = "yi"
            call uiDo(rc,move)
            UCorner = .true.
            return
        end if
        if (rc%U(3,1) == color) then
            move = "y"
            call uiDo(rc, move)
            UCorner = .true.
            return
        end if
        if (rc%U(1,1) == color) then
            move = "y"
            call uiDo(rc,move)
            call uiDo(rc,move)
            UCorner = .true.
            return
        end if
        UCorner = .false.
        return
    end function
        
    logical function FCorner(rc, ui)
        implicit none
        type(RubicCube) :: rc
        type(CommandLineInterface) :: ui
        character(len=1) :: color
        character(len=80) :: move
        color = rc%F(2,2)
        if (rc%F(3,3) == color) then
            move = "x"
            call uiDo(rc,move)
            FCorner=.true.
            return
        end if
        if (rc%F(3,1) == color) then
            move = "z"
            call uiDo(rc,move)
            move = "x"
            call uiDo(rc,move)
            FCorner=.true.
            return
        end if
        if (rc%F(1,3) == color) then
            move = "zi"
            call uiDo(rc,move)
            move = "x"
            call uiDo(rc,move)
            FCorner=.true.
            return
        end if
        if (rc%F(1,1) == color) then
            move = "z"
            call uiDo(rc,move)
            move = "z"
            call uiDo(rc,move)
            move = "x"
            call uiDo(rc,move)
            FCorner=.true.
            return
        end if
        FCorner=.false.
        return
    end function

    logical function LCorner(rc, ui)
        implicit none
        type(RubicCube) :: rc
        type(CommandLineInterface) :: ui
        character(len=1) :: color
        character(len=80) :: move
        color = rc%L(2,2)
        if (rc%L(3,1) == color) then
            move = "z"
            call uiDo(rc,move)
            LCorner=.true.
            return
        end if
        if (rc%L(1,1) == color) then
            move = "xi"
            call uiDo(rc,move)
            move = "z"
            call uiDo(rc,move)
            LCorner=.true.
            return
        end if
        if (rc%L(3,3) == color) then
            move = "x"
            call uiDo(rc,move)
            move = "z"
            call uiDo(rc,move)
            LCorner=.true.
            return
        end if
        if (rc%L(1,3) == color) then
            move = "x"
            call uiDo(rc,move)
            move = "x"
            call uiDo(rc,move)
            move = "z"
            call uiDo(rc,move)
            LCorner = .true.
            return
        end if
        LCorner = .false.
        return
    end function

    logical function RCorner(rc, ui)
        implicit none
        type(RubicCube) :: rc
        type(CommandLineInterface) :: ui
        character(len=1) :: color
        character(len=80) :: move
        color = rc%R(2,2)
        if (rc%R(1,3) == color) then
            move = "zi"
            call uiDo(rc,move)
            RCorner=.true.
            return
        end if
        if (rc%R(3,3) == color) then
            move = "x"
            call uiDo(rc,move)
            move = "zi"
            call uiDo(rc,move)
            RCorner=.true.
            return
        end if
        if (rc%R(1,1) == color) then
            move = "xi"
            call uiDo(rc,move)
            move = "zi"
            call uiDo(rc,move)
            RCorner=.true.
            return
        end if
        if (rc%R(3,1) == color) then
            move = "x"
            call uiDo(rc,move)
            move = "x"
            call uiDo(rc,move)
            move = "zi"
            call uiDo(rc,move)
            RCorner = .true.
            return
        end if
        RCorner = .false.
        return
    end function

    logical function BCorner(rc, ui)
        implicit none
        type(RubicCube) :: rc
        type(CommandLineInterface) :: ui
        character(len=1) :: color
        character(len=80) :: move
        color = rc%B(2,2)
        if (rc%B(3,1) == color) then
            move = "xi"
            call uiDo(rc,move)
            BCorner=.true.
            return
        end if
        if (rc%B(3,1) == color) then
            move = "zi"
            call uiDo(rc,move)
            move = "xi"
            call uiDo(rc,move)
            BCorner=.true.
            return
        end if
        if (rc%B(1,3) == color) then
            move = "z"
            call uiDo(rc,move)
            move = "xi"
            call uiDo(rc,move)
            BCorner=.true.
            return
        end if
        if (rc%L(1,1) == color) then
            move = "z"
            call uiDo(rc,move)
            move = "z"
            call uiDo(rc,move)
            move = "xi"
            call uiDo(rc,move)
            BCorner = .true.
            return
        end if
        BCorner = .false.
        return
    end function

    logical function DCorner(rc, ui)
        implicit none
        type(RubicCube) :: rc
        type(CommandLineInterface) :: ui
        character(len=1) :: color
        character(len=80) :: move
        color = rc%D(2,2)
        if (rc%D(3,3) == color) then
            move = "x"
            call uiDo(rc,move)
            move = "x"
            call uiDo(rc,move)
            DCorner=.true.
            return
        end if
        if (rc%L(3,1) == color) then
            move = "yi"
            call uiDo(rc,move)
            move = "x"
            call uiDo(rc,move)
            move = "x"
            call uiDo(rc,move)
            DCorner=.true.
            return
        end if
        if (rc%L(1,3) == color) then
            move = "y"
            call uiDo(rc,move)
            move = "x"
            call uiDo(rc,move)
            move = "x"
            call uiDo(rc,move)
            DCorner=.true.
            return
        end if
        if (rc%L(1,1) == color) then
            move = "y"
            call uiDo(rc,move)
            move = "y"
            call uiDo(rc,move)
            move = "x"
            call uiDo(rc,move)
            move = "x"
            call uiDo(rc,move)
            DCorner = .true.
            return
        end if
        DCorner = .false.
        return
    end function

    subroutine setDelay()
        implicit none
        integer :: ios
        logical delay
        print *, "Please choose whether you want instantaneous or ridiculously slow solutions. Integer sleep <3."
        read(5, *, iostat=ios) delay
        if (ios/=0) delay=.false.
        waitTime = delay
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
        print *, "Executing move ",move
        call execute(rc, move)
        print *, "Current status:"
        call printStr(rc)
        !Fortran sleep take time in seconds
        !..as integers. Why oh god why?
        if (waitTime) call sleep(1)
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
            call rMi(rc)
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
        case default 
            print *, move
            !For debugging purposes
            moveCount = moveCount-moveCount
            print *, 1/moveCount
        end select
        moveCount = moveCount + 1
    end subroutine

    subroutine p1a1(rc, ui)
        implicit none
        type(RubicCube) :: rc
        type(CommandLineInterface) :: ui
        character(len=80) :: Ri = "Ri", Di = "Di", R = "R"
        call uiDo(rc,Ri)
        call uiDo(rc,Di)
        call uiDo(rc,R)
    end subroutine

    subroutine p1a2(rc, ui)
        implicit none
        type(RubicCube) :: rc
        type(CommandLineInterface) :: ui
        character(len=80) :: Di="Di", Ri="Ri", D="D", R="R"
        call uiDo(rc,Di)
        call uiDo(rc,Ri)
        call uiDo(rc,D)
        call uiDo(rc,R)
    end subroutine

    subroutine p1a3(rc, ui)
        implicit none
        type(RubicCube) :: rc
        type(CommandLineInterface) :: ui
        character(len=80) :: Ri="Ri", D="D", R="R", Di="Di"
        call uiDo(rc,Ri)
        call uiDo(rc,D)
        call uiDo(rc,R)
        call uiDo(rc,D)
        call uiDo(rc,D)
        call uiDo(rc,Ri)
        call uiDo(rc,Di)
        call uiDo(rc,R)
    end subroutine

    subroutine p1a4(rc, ui)
        implicit none
        type(RubicCube) :: rc
        type(CommandLineInterface) :: ui
        character(len=80) :: F="F", D="D", Fi="Fi", Ri="Ri", R="R"
        call uiDo(rc,F)
        call uiDo(rc,D)
        call uiDo(rc,Fi)
        call uiDo(rc,D)
        call uiDo(rc,D)
        call uiDo(rc,Ri)
        call uiDo(rc,D)
        call uiDo(rc,R)
    end subroutine

    subroutine p1a5(rc, ui)
        implicit none
        type(RubicCube) :: rc
        type(CommandLineInterface) :: ui
        character(len=80) :: Ri="Ri", Di="Di", R="R", D="D"
        call uiDo(rc,Ri)
        call uiDo(rc,Di)
        call uiDo(rc,R)
        call uiDo(rc,D)
        call uiDo(rc,Ri)
        call uiDo(rc,Di)
        call uiDo(rc,R)
    end subroutine

    subroutine p2a1(rc, ui)
        implicit none
        type(RubicCube) :: rc
        type(CommandLineInterface) :: ui
        character(len=80) :: M="M", Di="Di", Mi="Mi"
        call uiDo(rc,M)
        call uiDo(rc,Di)
        call uiDo(rc,Di)
        call uiDo(rc,Mi)
    end subroutine

    subroutine p2a2(rc, ui)
        implicit none
        type(RubicCube) :: rc
        type(CommandLineInterface) :: ui
        character(len=80) :: Di="Di", M="M", D="D", Mi="Mi"
        call uiDo(rc,Di)
        call uiDo(rc,M)
        call uiDo(rc,D)
        call uiDo(rc,Mi)

    end subroutine

    subroutine p2a3(rc, ui)
        implicit none
        type(RubicCube) :: rc
        type(CommandLineInterface) :: ui
        character(len=80) :: E="E",F="F", Ei="Ei", Fi="Fi"
        call uiDo(rc,E)
        call uiDo(rc,F)
        call uiDo(rc,Ei)
        call uiDo(rc,Fi)
    end subroutine

    subroutine p2a4(rc, ui)
        implicit none
        type(RubicCube) :: rc
        type(CommandLineInterface) :: ui
        character(len=80) :: E="E", Fi="Fi", Ei="Ei", F="F"
        call uiDo(rc,E)
        call uiDo(rc,Fi)
        call uiDo(rc,Ei)
        call uiDo(rc,Ei)
        call uiDo(rc,F)

    end subroutine

    subroutine p2a5(rc, ui)
        implicit none
        type(RubicCube) :: rc
        type(CommandLineInterface) :: ui
        character(len=80) :: M="M", Di="Di", Mi="Mi", D="D"
        call uiDo(rc,M)
        call uiDo(rc,Di)
        call uiDo(rc,Di)
        call uiDo(rc,Mi)
        call uiDo(rc,Di)
        call uiDo(rc,M)
        call uiDo(rc,D)
        call uiDo(rc,Mi)


    end subroutine

    subroutine p3a1(rc, ui)
        implicit none
        type(RubicCube) :: rc
        type(CommandLineInterface) :: ui
        character(len=80) :: D="D", L="L", Di="Di", Li="Li", Fi="Fi", F="F"
        call uiDo(rc,D)
        call uiDo(rc,L)
        call uiDo(rc,Di)
        call uiDo(rc,Li)
        call uiDo(rc,Di)
        call uiDo(rc,Fi)
        call uiDo(rc,D)
        call uiDo(rc,F)
    end subroutine

    subroutine p3a2(rc, ui)
        implicit none
        type(RubicCube) :: rc
        type(CommandLineInterface) :: ui
        character(len=80) :: Di="Di", Ri="Ri", D="D", R="R", F="F", Fi="Fi"
        call uiDo(rc,Di)
        call uiDo(rc,Ri)
        call uiDo(rc,D)
        call uiDo(rc,R)
        call uiDo(rc,D)
        call uiDo(rc,F)
        call uiDo(rc,Di)
        call uiDo(rc,Fi)
    end subroutine

    subroutine p4a1(rc, ui)
        implicit none
        type(RubicCube) :: rc
        type(CommandLineInterface) :: ui
        character(len=80) :: Li="Li", rUi="Ui", L="L", F="F", U="U", Fi="Fi"
        call uiDo(rc,Li)
        call uiDo(rc,rUi)
        call uiDo(rc,L)
        call uiDo(rc,F)
        call uiDo(rc,U)
        call uiDo(rc,Fi)
        call uiDo(rc,Li)
        call uiDo(rc,U)
        call uiDo(rc,L)
        call uiDo(rc,U)
        call uiDo(rc,U)
    end subroutine

    subroutine p4a2(rc, ui)
        implicit none
        type(RubicCube) :: rc
        type(CommandLineInterface) :: ui
        character(len=80) :: y="y", U="U", Li="Li", rUi="Ui", L="L", F="F", Fi="Fi", yi="yi"
        call uiDo(rc,y)
        call uiDo(rc,U)
        call uiDo(rc,Li)
        call uiDo(rc,rUi)
        call uiDo(rc,L)
        call uiDo(rc,F)
        call uiDo(rc,U)
        call uiDo(rc,Fi)
        call uiDo(rc,Li)
        call uiDo(rc,U)
        call uiDo(rc,L)
        call uiDo(rc,U)
        call uiDo(rc,yi)
    end subroutine

    subroutine p5a1(rc, ui)
        implicit none
        type(RubicCube) :: rc
        type(CommandLineInterface) :: ui
        character(len=80) :: Li="Li", rUi="Ui", L="L"
        call uiDo(rc,Li)
        call uiDo(rc,rUi)
        call uiDo(rc,L)
        call uiDo(rc,rUi)
        call uiDo(rc,Li)
        call uiDo(rc,rUi)
        call uiDo(rc,rUi)
        call uiDo(rc,L)
        call uiDo(rc,rUi)
        call uiDo(rc,rUi)
    end subroutine

    subroutine p6a1(rc, ui)
        implicit none
        type(RubicCube) :: rc
        type(CommandLineInterface) :: ui
        character(len=80) :: Mi="Mi", rUi="Ui", M="M"
        call uiDo(rc,Mi)
        call uiDo(rc,rUi)
        call uiDo(rc,M)
        call uiDo(rc,rUi)
        call uiDo(rc,rUi)
        call uiDo(rc,Mi)
        call uiDo(rc,rUi)
        call uiDo(rc,M)
    end subroutine

    subroutine p7a1(rc, ui)
        implicit none
        type(RubicCube) :: rc
        type(CommandLineInterface) :: ui
        character(len=80) :: Ri = "Ri", Ei="Ei", rUi="Ui", R="R", E="E"
        call uiDo(rc,Ri)
        call uiDo(rc,Ei)
        call uiDo(rc,Ri)
        call uiDo(rc,Ri)
        call uiDo(rc,Ei)
        call uiDo(rc,Ei)
        call uiDo(rc,Ri)
        call uiDo(rc,rUi)
        call uiDo(rc,rUi)
        call uiDo(rc,R)
        call uiDo(rc,E)
        call uiDo(rc,E)
        call uiDo(rc,Ri)
        call uiDo(rc,Ri)
        call uiDo(rc,E)
        call uiDo(rc,R)
        call uiDo(rc,rUi)
        call uiDo(rc,rUi)
    end subroutine

    subroutine p7a2(rc, ui)
        implicit none
        type(RubicCube) :: rc
        type(CommandLineInterface) :: ui
        character(len=80) :: Fi = "Fi", Li = "Li", Ri = "Ri", Ei="Ei", rUi = "Ui", R="R", E="E", L="L", F="F"
        call uiDo(rc,Fi)
        call uiDo(rc,Li)
        call uiDo(rc,Ri)
        call uiDo(rc,Ei)
        call uiDo(rc,Ri)
        call uiDo(rc,Ri)
        call uiDo(rc,Ei)
        call uiDo(rc,Ei)
        call uiDo(rc,Ri)
        call uiDo(rc,rUi)
        call uiDo(rc,rUi)
        call uiDo(rc,R)
        call uiDo(rc,E)
        call uiDo(rc,E)
        call uiDo(rc,Ri)
        call uiDo(rc,Ri)
        call uiDo(rc,E)
        call uiDo(rc,R)
        call uiDo(rc,rUi)
        call uiDo(rc,rUi)
        call uiDo(rc,L)
        call uiDo(rc,F)
    end subroutine


end module solver

program RubicSolver
    use solver
    implicit none
    type(CommandLineInterface) :: cli
    cli = newCli()
    call doCliThings(cli)
end program RubicSolver
