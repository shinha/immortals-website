Rails.application.routes.draw do

  resources :events
  root 'welcome#index'
  get 'welcome/index'

  get 'welcome/login'
  
  get 'welcome/index2'

  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
