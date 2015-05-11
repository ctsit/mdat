# Miranda Algorithm for Calulating Fuzzy Measures

Excerpted from _E.F. Combarro, P. Miranda / Computers & Operations Research 33 (2006) 3046 – 3066_, pages 3060-3061

The method that we propose to obtain random fuzzy measures is presented in Algorithm 2.
					
Algorithm 2. Random generation of a fuzzy measure mu on a set X 

	mu(∅) := 0
	mu(X) := 1

	while there exists A ⊂ X such that mu(A) is undefined do randomly choose A ⊂ X such that mu(A) is undefined
		min := 0
		max := 1
		for every B ⊂ A such that mu(B) is defined do
			if mu(B)>min then
				min := mu(B)
			end if 
		end for
		for every B ⊃ A such that mu(B) is defined do 
			if mu(B) < max then
				max := mu(B)
			end if
		end for
		mu(A) := random value between min and max 
	end while 
