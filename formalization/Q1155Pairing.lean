import Std
namespace TransversalPairing
variable {Cell : Type}

/-- A matching may leave cells unpaired. Symmetry and uniqueness express
disjoint pairs, and irreflexivity prevents a cell being its own mate. -/
structure Matching (Cell : Type) where
  pair : Cell → Cell → Prop
  symm : ∀ {a b}, pair a b → pair b a
  unique : ∀ {a b c}, pair a b → pair a c → b = c
  different : ∀ {a b}, pair a b → a ≠ b

def add (p : Cell → Prop) (a : Cell) (i : Cell) := i = a ∨ p i

/-- At the start of each first-player turn, each mate of an owned cell
belongs to the defender. -/
def guarded (M : Matching Cell) (first second : Cell → Prop) :=
  ∀ a b, M.pair a b → first a → second b

theorem move_cannot_complete (M : Matching Cell) (first second : Cell → Prop)
    (g : guarded M first second) (disjoint : ∀ i, first i → ¬second i)
    (a : Cell) (available : ¬second a) :
    ∀ i j, M.pair i j → ¬ (add first a i ∧ add first a j) := by
  intro i j pair both
  rcases both with ⟨hi,hj⟩
  rcases hi with rfl | hi <;> rcases hj with rfl | hj
  · exact M.different pair rfl
  · exact available (g _ _ (M.symm pair) hj)
  · exact available (g _ _ pair hi)
  · exact disjoint _ hj (g _ _ pair hi)

/-- Each legal first move has a defensive reply set: take its unique free
mate if one exists. The set may be empty, allowing any otherwise legal
fallback move or an exhausted board. -/
def response (M : Matching Cell) (first second : Cell → Prop) (a b : Cell) :=
  M.pair a b ∧ ¬first b ∧ ¬second b

theorem response_unique (M : Matching Cell) (f s : Cell → Prop) (a b c : Cell)
    (hb : response M f s a b) (hc : response M f s a c) : b = c :=
  M.unique hb.1 hc.1

theorem step (M : Matching Cell) (f s : Cell → Prop) (a : Cell)
    (g : guarded M f s) (available : ¬s a) :
    guarded M (add f a) (fun b => s b ∨ response M f s a b) := by
  intro i j pair hi
  rcases hi with rfl | hi
  · by_cases old : s j
    · exact Or.inl old
    · exact Or.inr ⟨pair, fun h => available (g _ _ (M.symm pair) h), old⟩
  · exact Or.inl (g _ _ pair hi)

theorem guarded_monotone (M : Matching Cell) (f s t : Cell → Prop)
    (g : guarded M f s) (grow : ∀ b, s b → t b) : guarded M f t :=
  fun a b h hf => grow b (g a b h hf)

/-- A history may include an extra legal fallback mark when there is no free
mate. Only the response invariant is needed to obtain the no-pair conclusion. -/
inductive History (M : Matching Cell) : (Cell → Prop) → (Cell → Prop) → Prop
  | start : History M (fun _ => False) (fun _ => False)
  | next {f s : Cell → Prop} (prev : History M f s) (a : Cell) (free : ¬s a)
      (t : Cell → Prop) (extendsSecond : ∀ b, s b ∨ response M f s a b → t b) :
      History M (add f a) t

theorem all_turns (M : Matching Cell) {f s : Cell → Prop} (h : History M f s) :
    guarded M f s := by
  induction h with
  | start => intro _ _ _ hf; exact hf.elim
  | next prev a free t grow ih =>
    exact guarded_monotone M _ _ _ (step M _ _ a ih free) grow

#print axioms all_turns
#print axioms move_cannot_complete
#print axioms step
end TransversalPairing
