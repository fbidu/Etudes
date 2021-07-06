#lang slideshow

(define (square n)
  ; Hey all :D
  ; Comments are great!
  (filled-rectangle n n #:color "Thistle"))

; Local Binding

(define (four p)
  (define two-p (hc-append p p)) ; Local binding with define
  (vc-append two-p two-p)) ; see? Using it here

; Local Binding with let
(define (checker p1 p2)
  (let ([p12 (hc-append p1 p2)]
        [p21 (hc-append p2 p1)]) ; Multiple bindings!
    (vc-append p12 p21)))

(checker (colorize (square 100) "red")
         (colorize (square 100) "black"))

; let* lets later bindings refer to earlier bindings
(define (checkerboard p)
  (let* ([rp (colorize p "red")]
         [bp (colorize p "black")]
         [c (checker rp bp)] ; gotcha!
         [c4 (four c)])
   (four c4)))

(checkerboard (square 10))

; 6 Functions are Values