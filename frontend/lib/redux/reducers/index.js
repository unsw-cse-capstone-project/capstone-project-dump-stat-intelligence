import { combineReducers } from 'redux';
import { authReducer } from './authReducer';
import { pantryReducer } from './pantryReducer';
import { queryReducer } from './queryReducer';

export default combineReducers({
    auth : authReducer,
    pantry : pantryReducer,
    query : queryReducer

});