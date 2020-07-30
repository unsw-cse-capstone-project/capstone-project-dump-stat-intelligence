import Link from "next/link";
import styles from "./RecipeCard.module.scss";

import Indicator from "./Indicator";

export default function RecipeCard(props) {
  return (
    <Link href={`/recipe/[recipeId]`} as={`/recipe/${props.recipe.id}`}>
      <div className={"card " + styles.recipe}>
        <div className="card-image">
          <figure className="image is-4by3">
            <img style={{"objectFit":"cover"}} src={props.recipe.image_URL === null ? `https://source.unsplash.com/400x300/?food&sig=${props.recipe.id}` : props.recipe.image_URL} alt={props.recipe.name} />
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
          {
            props.recipe.missing_ing ?
            <Indicator perfect={props.recipe.missing_ing.length === 0} value={props.recipe.missing_ing.length} color="#0f0">
              <ul className={styles.missList}>
                {props.recipe.missing_ing.map((val, idx) => (
                      <li key={idx}>
                        -&nbsp;&nbsp;{val}
                      </li>
                ))}
              </ul>
            </Indicator>
            : ""
          }
        </div>
      </div>
    </Link>
  );
}
