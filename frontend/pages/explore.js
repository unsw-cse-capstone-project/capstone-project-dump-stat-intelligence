import Head from "next/head";
import React, { useState } from "react";

import { useSelector, useDispatch } from "react-redux";
import { recipes_update } from "../lib/redux/actions/recipesAction";

import RecipeCard from "../components/RecipeCard/RecipeCard";
import Filter from "../components/Pantry/Filter";

export default function Explore() {
  const recipes = useSelector((state) => state.recipes.recipes);
  const filter = useSelector((state) => state.explore.filters);
  const dispatch = useDispatch();

  const [filteredRecipes, setFilteredRecipes] = useState(recipes);

  // Only occurs once
  React.useEffect(() => {
    dispatch(recipes_update());
  }, []);

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
                <RecipeCard recipe={recipe} />
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
