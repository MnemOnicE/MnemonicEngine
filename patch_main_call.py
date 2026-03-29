<<<<<<< SEARCH
    args = parser.parse_args()

    if not args.task and not args.file:
        parser.print_help()
        sys.exit(0)

    task = args.task or f"Process file: {args.file}"

    # Configure centralized logging
=======
    args = parser.parse_args()

    if not args.task and not args.file:
        # Default behavior: run the game
        start_game()
        sys.exit(0)

    task = args.task or f"Process file: {args.file}"

    # Configure centralized logging
>>>>>>> REPLACE
