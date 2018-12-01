

	program dat

	implicit none
	

	double precision sig,rsig,logSig,inc,ML,Vc,qual,logMaj,logRe,logHalf
	double precision logG,conc,eps,logLum
	character*20	galaxy
	integer i

	open(unit=1, file='Capellari2013.dat')
	open(unit=2, file='mass_Sig.out')

	do i=1,1000
		read(1,*,end=10) galaxy,sig,rsig,logSig,inc,ML,Vc,qual,logMaj,logRe,logHalf,logG,conc,eps,logLum
		!write(2,*) logLum,sig
		write(2,*) log10((10**logLum)*(10**ML)),sig
	
	enddo
10	continue


	close(1)
	close(2)
	end
