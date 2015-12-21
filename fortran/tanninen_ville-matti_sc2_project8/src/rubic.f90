module Rubic

    type::RubicCube
        character(len=1),dimension(3,3) :: F,L,R,U,D,B
    end type RubicCube

contains

    type(RubicCube) function newRC()
        implicit none
        newRC%F = "R"
        newRC%L = "Y"
        newRC%R = "W"
        newRC%U = "G"
        newRC%D = "B"
        newRC%B = "O"
    end function

    character(len=500) function str(rc)
        implicit none
        type(RubicCube), intent(in) :: rc
        character(len=7) :: indent = "       "
        character(len=20) :: row
        integer :: i, j

        do i=1, 3
            write(row, '(A1, x)') rc%F(1:3, i)
            str = trim(str)//indent &
                //trim(row)//"\n"
        end do
        str = trim(str)//"\n"
        do i=1, 3
            write(row, '(3(A1,x), x)') &
                 rc%L(1:3, i), rc%F(1:3, i), &
                 rc%R(1:3, i)
            str = trim(str)//trim(row)//"\n"
        end do
        str = trim(str)//"\n"
        do i=1, 3
            write(row, '(A1, x)') rc%D(1:3, i)
            str = trim(str)//indent &
                //trim(row)//"\n"
        end do
        do i=1, 3
            write(row, '(A1, x)') rc%B(1:3, i)
            str = trim(str)//indent &
                //trim(row)//"\n"
        end do
    end function

    !Rotates a face of the cube - and only
    !the face! - 90 degrees clockwise.
    function rFace(face)
        implicit none
        character(len=1),dimension(3,3) :: rFace
        character(len=1),dimension(3,3),intent(in) :: face
        integer :: i, j
        
        do i=1, 3
            do j=1, 3
                rFace(j,i) = face(i, 2-j)
            end do
        end do
    end function

    !Rotates a face of the cube - and only
    !the face! -90 degrees counter-clockwise
    function rFacei(face)
        implicit none
        character(len=1),dimension(3,3) :: rFacei
        character(len=1),dimension(3,3),intent(in) :: face
        rFacei = rFace(face)
        rFacei = rFace(rFacei)
        rFacei = rFace(rFacei)
    end function

    function iFaceY(face)
        implicit none
        character(len=1),dimension(3,3) :: iFaceY
        character(len=1),dimension(3,3),intent(in) :: face
        iFaceY = face(1:3, 3:1:-1)
    end function

    function iFaceX(face)
        implicit none
        character(len=1),dimension(3,3) :: iFaceX
        character(len=1),dimension(3,3),intent(in) :: face
        iFaceX = face(3:1:-1, 1:3)
    end function

    !Rotates the entire cube clockwise on R
    subroutine x(rc)
        implicit none
        type(RubicCube) :: rc
        character(len=1),dimension(3,3) :: temp
        rc%R = rFace(rc%R)
        rc%L = rFacei(rc%L)
        temp = rc%U
        rc%U = rc%F
        rc%F = rc%D
        rc%D = rc%B
        rc%B = temp
    end subroutine

    !Rotates the entire cube counter-clockwise on R
    subroutine xi(rc)
        implicit none
        type(RubicCube) :: rc
        call x(rc)
        call x(rc)
        call x(rc)
    end subroutine

    !Rotates the entire cube clockwise on U
    subroutine y(rc)
        implicit none
        type(RubicCube) :: rc
        character(len=1),dimension(3,3) :: temp
        rc%U = rFace(rc%U)
        rc%D = rFacei(rc%D)
        temp = iFaceX(iFaceY(rc%L))
        rc%L = rc%F
        rc%F = rc%R
        rc%R = iFaceX(iFaceY(rc%B))
        rc%B = temp
    end subroutine

    !Rotates the entire cube counter-clockwise on U
    subroutine yi(rc)
        implicit none
        type(RubicCube) :: rc
        call y(rc)
        call y(rc)
        call y(rc)
    end subroutine

    !Rotates the entire cube clockwise on F
    subroutine z(rc)
        implicit none
        type(RubicCube) :: rc
        character(len=1),dimension(3,3) :: temp
        rc%F = rFace(rc%F)
        rc%B = rFacei(rc%B)
        temp = rFace(rc%U)
        rc%U = rFace(rc%L)
        rc%L = rFace(rc%D)
        rc%D = rFace(rc%R)
        rc%R = temp
    end subroutine

    !Rotates the entire cube counter-clockwise on F
    subroutine zi(rc)
        implicit none
        type(RubicCube) :: rc
        call z(rc)
        call z(rc)
        call z(rc)
    end subroutine

    !In general, rotations are named as follows:
    !r for rotation
    !Side name
    !Without i: clockwise
    !With i: counter-clockwise
    !Without w: only one layer
    !With w: also the corresponding middle layer

    subroutine rF(rc)
        implicit none
        character(len=1),dimension(3) :: temp
        type(RubicCube) :: rc
        rc%F = rFace(rc%F)
        temp = rc%U(1:3, 3)
        rc%U(1:3, 3) = rc%L(3, 3:1:-1)
        rc%L(3, 3:1:-1) = rc%D(1:3, 1)
        rc%D(1:3, 1) = rc%R(1, 3:1:-1)
        rc%R(1, 1:3) = temp
    end subroutine

    subroutine rFi(rc)
        implicit none
        type(RubicCube) :: rc
        call rF(rc)
        call rF(rc)
        call rF(rc)
    end subroutine

    subroutine rFw(rc)
        implicit none
        character(len=1),dimension(3) :: temp
        type(RubicCube) :: rc
        call rF(rc)
        temp = rc%U(1:3, 2)
        rc%U(1:3, 2) = rc%L(2, 3:1:-1)
        rc%L(2, 1:3) = rc%D(1:3, 2)
        rc%D(1:3, 2) = rc%R(2, 3:1:-1)
        rc%R(2, 1:3) = temp
    end subroutine

    subroutine rFiw(rc)
        implicit none
        type(RubicCube) :: rc
        call rFw(rc)
        call rFw(rc)
        call rFw(rc)
    end subroutine

    subroutine rL(rc)
        implicit none
        type(RubicCube) :: rc
        call yi(rc)
        call rF(rc)
        call y(rc)
    end subroutine

    subroutine rLi(rc)
        implicit none
        type(RubicCube) :: rc
        call y(rc)
        call rFi(rc)
        call y(rc)
    end subroutine

    subroutine rLw(rc)
        implicit none
        type(RubicCube) :: rc
        call yi(rc)
        call rFw(rc)
        call y(rc)
    end subroutine

    subroutine rLi2(rc)
        implicit none
        type(RubicCube) :: rc
        call yi(rc)
        call rFiw(rc)
        call y(rc)
    end subroutine

    subroutine rR(rc)
        implicit none
        type(RubicCube) :: rc
        call y(rc)
        call rF(rc)
        call yi(rc)
    end subroutine

    subroutine rRi(rc)
        implicit none
        type(RubicCube) :: rc
        call y(rc)
        call rFi(rc)
        call yi(rc)
    end subroutine

    subroutine rRw(rc)
        implicit none
        type(RubicCube) :: rc
        call y(rc)
        call rFw(rc)
        call yi(rc)
    end subroutine

    subroutine rRiw(rc)
        implicit none
        type(RubicCube) :: rc
        call y(rc)
        call rFiw(rc)
        call yi(rc)
    end subroutine

    subroutine rU(rc)
        implicit none
        type(RubicCube) :: rc
        call xi(rc)
        call rF(rc)
        call x(rc)
    end subroutine

    subroutine rUi(rc)
        implicit none
        type(RubicCube) :: rc
        call xi(rc)
        call rFi(rc)
        call x(rc)
    end subroutine

    subroutine rUw(rc)
        implicit none
        type(RubicCube) :: rc
        call xi(rc)
        call rFw(rc)
        call x(rc)
    end subroutine

    subroutine rUiw(rc)
        implicit none
        type(RubicCube) :: rc
        call xi(rc)
        call rFiw(rc)
        call x(rc)
    end subroutine

    subroutine rD(rc)
        implicit none
        type(RubicCube) :: rc
        call x(rc)
        call rF(rc)
        call xi(rc)
    end subroutine

    subroutine rDi(rc)
        implicit none
        type(RubicCube) :: rc
        call x(rc)
        call rFi(rc)
        call xi(rc)
    end subroutine

    subroutine rDw(rc)
        implicit none
        type(RubicCube) :: rc
        call x(rc)
        call rFw(rc)
        call xi(rc)
    end subroutine

    subroutine rDiw(rc)
        implicit none
        type(RubicCube) :: rc
        call x(rc)
        call rFiw(rc)
        call xi(rc)
    end subroutine

    subroutine rB(rc)
        implicit none
        type(RubicCube) :: rc
        call y(rc)
        call y(rc)
        call rF(rc)
        call y(rc)
        call y(rc)
    end subroutine

    subroutine rBi(rc)
        implicit none
        type(RubicCube) :: rc
        call y(rc)
        call y(rc)
        call rFi(rc)
        call y(rc)
        call y(rc)
    end subroutine

    subroutine rBw(rc)
        implicit none
        type(RubicCube) :: rc
        call y(rc)
        call y(rc)
        call rFw(rc)
        call y(rc)
        call y(rc)
    end subroutine

    subroutine rBiw(rc)
        implicit none
        type(RubicCube) :: rc
        call y(rc)
        call y(rc)
        call rFiw(rc)
        call y(rc)
        call y(rc)
    end subroutine

    !E or equator is the layer between U and D
    !Turn direction same as D
    subroutine rE(rc)
        implicit none
        type(RubicCube) :: rc
        call rDw(rc)
        call rDi(rc)
    end subroutine

    subroutine rEi(rc)
        implicit none
        type(RubicCube) :: rc
        call rDiw(rc)
        call rD(rc)
    end subroutine

    !M or middle is the layer between L and R
    !Turn direction same as L
    subroutine rM(rc)
        implicit none
        type(RubicCube) :: rc
        call rLw(rc)
        call rLi(rc)
    end subroutine

    subroutine rMi(rc)
        implicit none
        type(RubicCube) :: rc
        call rLiw(rc)
        call rL(rc)
    end subroutine

    !S or standing is the layer between F and B
    !Turn direction same as F
    subroutine rS(rc)
        implicit none
        type(RubicCube) :: rc
        call rFw(rc)
        call rFi(rc)
    end subroutine

    subroutine rSi(rc)
        implicit none
        type(RubicCube) :: rc
        call rFiw(rc)
        call rF(rc)
    end subroutine

end module Rubic
