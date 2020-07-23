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

  // Reruns on every re-render
  React.useEffect(() => {
    // setFilteredRecipes(getFilteredRecipes());
  });

  const getFilteredRecipes = () => {
    let filtereds = recipes.filter((r) => {
      for (let meal of Object.keys(filter.meal)) {
        if (filter.meal[meal]) {
          if (r.meal_cat.filter((m) => meal == m.name).length == 0) {
            return false;
          }
        }
      }

      for (let diet of Object.keys(filter.diet)) {
        if (filter.diet[diet]) {
          if (r.diet_req.filter((d) => diet == d.name).length == 0) {
            return false;
          }
        }
      }

      return true;
    });

    return filtereds;
  };

  // NOTE: unsure where filtering should really be happening?
  // Should it happen here or in the actual redux store?
  // Going to do it here for now

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
            getFilteredRecipes().map((recipe, idx) => (
              <div key={idx} className="column is-3">
                <RecipeCard
                  className="column is-3"
                  src={`https://source.unsplash.com/400x300/?food&sig=${recipe.id}`}
                  recipe={recipe}
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
