import Head from "next/head";
import React from "react";

import RecipeAPI from "../lib/api/recipe";

import { useSelector } from "react-redux";
import RecipeCard from "../components/RecipeCard/RecipeCard";

export default function Explore() {
  const recipes = useSelector((state) => state.recipes.recipes);
  console.log(recipes);
  return (
    <>
      <Head>
        <title>Pantry Pirate | Explore</title>
      </Head>
      <div>
        <br />
        <h1 className="title is-2">Explore Recipes</h1>
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
