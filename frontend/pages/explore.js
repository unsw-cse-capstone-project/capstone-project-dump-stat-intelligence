import Head from "next/head";
import React from "react";


import RecipeAPI from "../lib/api/recipe";

import { useSelector } from 'react-redux'; 
import RecipeCard from "../components/RecipeCard/RecipeCard";
import Filter from "../components/Pantry/Filter";

export default function Home() {
  const recipes = useSelector(state => state.recipes.recipes);
  return (
    <>
      <Head>
        <title>Pantry Pirate | Explore</title>
      </Head>
      <div>
        <br />
        <h1 className="title is-2">Explore Recipes</h1>
        <Filter/>
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


