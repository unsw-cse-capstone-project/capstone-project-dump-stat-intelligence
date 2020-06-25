import Head from "next/head";

import RecipeCard from "../components/RecipeCard/RecipeCard";

export default function Home() {
  const recipes = [
    "Sushi",
    "Dumplings",
    "Shepard's Pie",
    "another one",
    "Hello world",
  ];
  return (
    <div>
      <Head>
        <title>Pantry Pirate | Explore</title>
      </Head>
      <div>
        <h1 className="title">Explore Recipes</h1>
        <div className="columns is-multiline">
          {recipes.map((recipe, idx) => (
            <div key={idx} className="column is-3">
              <RecipeCard
                className="column is-3"
                src={`https://source.unsplash.com/400x300/?food&sig=${recipe}`}
                title={recipe}
                id={idx} // TODO: alter
              />
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
