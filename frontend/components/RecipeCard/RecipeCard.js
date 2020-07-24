import Link from "next/link";
import styles from "./RecipeCard.module.scss";

import Indicator from "./Indicator";

export default function RecipeCard(props) {
  return (
    <Link href={`/recipe/[recipeId]`} as={`/recipe/${props.recipe.id}`}>
      <div className={"card " + styles.recipe}>
        <div className="card-image">
          <figure className="image is-4by3">
            <img src={props.src} alt={props.recipe.name} />
          </figure>
        </div>
        <div className="card-content">
          <h4 className="title is-5" style={{ textAlign: "center" }}>
            {props.recipe.name}
          </h4>
          <p>
            {props.recipe.author.username} | {props.recipe.cook_time}
          </p>
          <p className="tags">
            {props.recipe.diet_req.map((req, idx) => (
              <span key={idx} className="tag is-light">
                {req.name}
              </span>
            ))}
            {props.recipe.meal_cat.map((req, idx) => (
              <span key={idx} className="tag is-dark">
                {req.name}
              </span>
            ))}
          </p>
          <Indicator value={props.recipe.ingredients.length} color="#0f0">
            <ul>
              {props.recipe.ingredients.map((ingredient, idx) => (
                    <li key={idx}>
                      {ingredient.ingredient.name}
                    </li>
              ))}
            </ul>
          </Indicator>
        </div>
      </div>
    </Link>
  );
}
