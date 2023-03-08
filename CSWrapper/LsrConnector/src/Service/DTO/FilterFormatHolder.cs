namespace LsrConnector.Service.DTO;

public readonly struct FilterFormatHolder
{
    private readonly string _exe = "Exe Files (.exe)|*.exe|All Files (*.*)|*.*";
    private readonly string _lsr = "PowerMill (*.lsr ) |*.lsr; | Other files (*.*)|*.*";
    private readonly FilterFormatEnum _requiredFormat;
    

    public FilterFormatHolder(FilterFormatEnum format)
    {
        _requiredFormat = format;
    }

    public override string ToString()
    {
        if (_requiredFormat == FilterFormatEnum.Exe)
        {
            return _exe;
        }

        return _lsr;
    }
}

public enum FilterFormatEnum
{
    Exe,
    Lsr
}