import Head from "next/head";
import React from "react";

import { useSelector, useDispatch } from "react-redux";
import { recipes_update } from "../lib/redux/actions/recipesAction";

import RecipeCard from "../components/RecipeCard/RecipeCard";
import Filter from "../components/Pantry/Filter";

export default function Explore() {
  const recipes = useSelector((state) => state.recipes.recipes);
  const dispatch = useDispatch();

  React.useEffect(() => {
    console.log("get all recipes");
    dispatch(recipes_update());
  }, []); // See https://reactjs.org/docs/hooks-effect.html#tip-optimizing-performance-by-skipping-effects for why that 2nd "[]" parameter

  return (
    <>
      <Head>
        <title>Pantry Pirate | Explore</title>
      </Head>
      <div>
        <br />
        <h1 className="title is-2">Explore Recipes</h1>
        <Filter />
        <div className="columns is-multiline">
          {recipes ? (
            recipes.map((recipe, idx) => (
              <div key={idx} className="column is-3">
                <RecipeCard
                  className="column is-3"
                  src={`https://source.unsplash.com/400x300/?food&sig=${recipe.id}`}
                  title={recipe.name}
                  id={recipe.id} // TODO: alter
                />
              </div>
            ))
          ) : (
            <p>Loading...</p>
          )}
        </div>
      </div>
    </>
  );
}
